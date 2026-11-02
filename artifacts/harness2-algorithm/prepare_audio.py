"""Generate narration, music bed, timeline and subtitles for the Harness² explainer."""
import argparse
import asyncio
import json
import subprocess
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
WORK = ROOT / '_build'
SCRIPT = json.loads((ROOT / 'script.json').read_text())
SR = 48000
GAP = 0.42          # silence between lines
SCENE_HEAD = 0.7    # silence before the first line of a scene
SCENE_TAIL = 0.9    # hold after the last line of a scene


def run(args):
    return subprocess.run(args, check=True, capture_output=True)


def read_audio(path):
    raw = run(['ffmpeg', '-v', 'error', '-i', str(path), '-f', 'f32le',
               '-ac', '1', '-ar', str(SR), '-']).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def write_wav(path, signal, channels=1):
    data = np.clip(signal, -1, 1).astype(np.float32)
    run_input = subprocess.run(
        ['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ac', str(channels), '-ar', str(SR),
         '-i', '-', str(path)], input=data.tobytes(), check=True, capture_output=True)
    return run_input


async def synthesize(text, path):
    import edge_tts
    voice = edge_tts.Communicate(text, SCRIPT['voice'], rate=SCRIPT['rate'], pitch='-2Hz')
    await voice.save(str(path))


def tts(engine):
    clips = []
    for si, scene in enumerate(SCRIPT['scenes']):
        for li, line in enumerate(scene['lines']):
            spoken = line.get('say', line['text'])
            if engine == 'edge':
                path = WORK / f'voice-{si:02d}-{li:02d}.mp3'
                if not path.exists():
                    asyncio.run(synthesize(spoken, path))
            else:
                path = WORK / f'voice-{si:02d}-{li:02d}.aiff'
                if not path.exists():
                    run(['say', '-v', 'Reed (Chinese (China mainland))', '-o', str(path), spoken])
            clips.append((si, li, read_audio(path)))
    return clips


def trim(signal, threshold=0.004):
    idx = np.where(np.abs(signal) > threshold)[0]
    if len(idx) == 0:
        return signal
    start = max(0, idx[0] - int(0.03 * SR))
    end = min(len(signal), idx[-1] + int(0.08 * SR))
    return signal[start:end]


def timeline(clips):
    cursor = 0.0
    scenes = []
    pieces = []
    by_scene = {}
    for si, li, audio in clips:
        by_scene.setdefault(si, []).append((li, trim(audio)))
    for si, scene in enumerate(SCRIPT['scenes']):
        start = cursor
        cursor += SCENE_HEAD
        lines = []
        for li, audio in by_scene[si]:
            duration = len(audio) / SR
            lines.append({'start': round(cursor - start, 3), 'end': round(cursor - start + duration, 3),
                          'text': scene['lines'][li]['text']})
            pieces.append((cursor, audio))
            cursor += duration + GAP
        cursor += SCENE_TAIL - GAP
        scenes.append({'id': scene['id'], 'start': round(start, 3), 'duration': round(cursor - start, 3),
                       'lines': lines})
    total = cursor
    voice = np.zeros(int(total * SR) + SR, dtype=np.float32)
    for at, audio in pieces:
        offset = int(at * SR)
        voice[offset:offset + len(audio)] += audio
    return scenes, voice[:int(total * SR)], total


def music_bed(voice, total):
    """Original slow pad (Am - F - C - G), ducked under narration."""
    n = len(voice)
    t = np.arange(n) / SR
    chords = [[220.0, 261.63, 329.63], [174.61, 220.0, 261.63],
              [196.0, 261.63, 329.63], [196.0, 246.94, 293.66]]
    bar = 4.0
    pad = np.zeros(n, dtype=np.float64)
    for ci in range(int(total / bar) + 1):
        s, e = int(ci * bar * SR), min(n, int((ci + 1) * bar * SR + 0.8 * SR))
        if s >= n:
            break
        seg_t = np.arange(e - s) / SR
        env = np.minimum(1, seg_t / 0.9) * np.minimum(1, np.maximum(0, (bar + 0.8 - seg_t) / 1.2))
        tone = sum(np.sin(2 * np.pi * f * seg_t) + 0.3 * np.sin(2 * np.pi * 2 * f * seg_t + 0.4)
                   for f in chords[ci % 4])
        pad[s:e] += tone * env / 4
    # soft pulse every half bar
    pulse = 0.25 * np.sin(2 * np.pi * 110 * t) * np.exp(-((t % 2.0) / 0.35))
    music = (pad + pulse) * 0.06
    # duck: envelope follower on the voice
    win = int(0.25 * SR)
    energy = np.convolve(np.abs(voice), np.ones(win) / win, mode='same')
    active = np.clip(energy / 0.02, 0, 1)
    smooth_win = int(0.4 * SR)
    active = np.convolve(active, np.ones(smooth_win) / smooth_win, mode='same')
    gain = 1.0 - 0.72 * active
    fade = np.minimum(1, t / 2.0) * np.minimum(1, (total - t) / 2.5)
    return (music * gain * fade).astype(np.float32)


def fmt(seconds, sep):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}'


def subtitles(scenes):
    cues = []
    for scene in scenes:
        for line in scene['lines']:
            cues.append((scene['start'] + line['start'], scene['start'] + line['end'] + 0.25, line['text']))
    srt, vtt = [], ['WEBVTT', '']
    for i, (a, b, text) in enumerate(cues, 1):
        srt += [str(i), f'{fmt(a, ",")} --> {fmt(b, ",")}', text, '']
        vtt += [f'{fmt(a, ".")} --> {fmt(b, ".")}', text, '']
    (ROOT / 'subtitles.srt').write_text('\n'.join(srt))
    (ROOT / 'subtitles.vtt').write_text('\n'.join(vtt))
    return len(cues)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--engine', choices=['edge', 'say'], default='edge')
    args = parser.parse_args()
    WORK.mkdir(exist_ok=True)
    (ROOT / 'audio').mkdir(exist_ok=True)
    scenes, voice, total = timeline(tts(args.engine))
    music = music_bed(voice, total)
    write_wav(WORK / 'narration.wav', voice)
    write_wav(WORK / 'music.wav', music)
    write_wav(WORK / 'mix-raw.wav', voice + music)
    run(['ffmpeg', '-v', 'error', '-y', '-i', str(WORK / 'mix-raw.wav'),
         '-af', 'loudnorm=I=-16:TP=-1.5:LRA=9', '-ar', str(SR), '-ac', '2', str(WORK / 'mix.wav')])
    for name in ('narration', 'music'):
        run(['ffmpeg', '-v', 'error', '-y', '-i', str(WORK / f'{name}.wav'),
             '-c:a', 'aac', '-b:a', '160k', str(ROOT / 'audio' / f'{name}.m4a')])
    cue_count = subtitles(scenes)
    (ROOT / 'timeline.json').write_text(json.dumps(
        {'engine': args.engine, 'voice': SCRIPT['voice'] if args.engine == 'edge' else 'Reed',
         'total': round(total, 3), 'scenes': scenes}, ensure_ascii=False, indent=2) + '\n')
    print(f'total={total:.2f}s scenes={len(scenes)} cues={cue_count}')


if __name__ == '__main__':
    main()

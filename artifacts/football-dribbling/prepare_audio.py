"""Build timed narration, subtitles and an original subdued sports music bed."""
import argparse
import asyncio
import json
import subprocess
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / 'video.json').read_text())
WORK = ROOT / '_build'
SR = 48000


def run(args):
    return subprocess.run(args, check=True, capture_output=True)


def read_audio(path):
    result = run(['ffmpeg', '-v', 'error', '-i', str(path), '-f', 'f32le',
                  '-ac', '1', '-ar', str(SR), '-'])
    return np.frombuffer(result.stdout, dtype='<f4').copy()


def write_audio(path, signal):
    with wave.open(str(path), 'wb') as out:
        out.setnchannels(1 if signal.ndim == 1 else signal.shape[1])
        out.setsampwidth(2)
        out.setframerate(SR)
        out.writeframes((np.clip(signal, -1, 1) * 32767).astype('<i2').tobytes())


async def synthesize(engine):
    WORK.mkdir(exist_ok=True)
    for i, scene in enumerate(CONFIG['scenes']):
        for j, line in enumerate(scene['lines']):
            suffix = 'mp3' if engine == 'edge' else 'aiff'
            path = WORK / f'voice-{engine}-{i:02}-{j:02}.{suffix}'
            if path.exists() and path.stat().st_size > 1000:
                continue
            if engine == 'edge':
                import edge_tts
                voice = edge_tts.Communicate(line, CONFIG['voice'], rate='+0%', pitch='-2Hz')
                await asyncio.wait_for(voice.save(str(path)), timeout=35)
            else:
                run(['say', '-v', 'Reed (Chinese (China mainland))', '-r', '225',
                     '-o', str(path), line])
            print(f'voice {i+1:02}/{len(CONFIG["scenes"])} line {j+1}: ready', flush=True)


def assemble(engine):
    voice = np.zeros(int(SR * CONFIG['duration']), dtype=np.float32)
    cues = []
    stats = []
    for i, scene in enumerate(CONFIG['scenes']):
        suffix = 'mp3' if engine == 'edge' else 'aiff'
        clips = [read_audio(WORK / f'voice-{engine}-{i:02}-{j:02}.{suffix}')
                 for j in range(len(scene['lines']))]
        # Trim only the leading/trailing digital silence, retaining 60 ms of breathing room.
        for j, clip in enumerate(clips):
            active = np.flatnonzero(np.abs(clip) > .003)
            if not active.size:
                raise ValueError(f'Empty speech: {i}/{j}')
            clips[j] = clip[max(0, active[0]-int(.06*SR)):min(len(clip), active[-1]+int(.09*SR))]
        total = sum(len(c)/SR for c in clips)
        available = scene['end']-scene['start']-.7-.22*(len(clips)-1)
        speed = max(.88, total/available)
        if speed > 1.24:
            raise ValueError(f'Scene {scene["id"]} too dense: {total:.2f}s / {available:.2f}s; shorten narration')
        if abs(speed-1) > .001:
            for j, clip in enumerate(clips):
                raw = WORK / f'tempo-{i:02}-{j:02}.wav'
                adjusted = WORK / f'adjusted-{i:02}-{j:02}.wav'
                write_audio(raw, clip)
                run(['ffmpeg','-v','error','-y','-i',str(raw),'-af',f'atempo={speed:.6f}',str(adjusted)])
                clips[j] = read_audio(adjusted)
        used = sum(len(c)/SR for c in clips)
        gap = min(.4, max(.22, (scene['end']-scene['start']-used-.7)/max(1,len(clips)-1)))
        cursor = scene['start'] + .35
        for line, clip in zip(scene['lines'], clips):
            begin = int(cursor*SR)
            voice[begin:begin+len(clip)] = clip
            finish = cursor+len(clip)/SR
            cues.append({'start':round(cursor,3),'end':round(finish,3),'text':line,'scene':scene['id']})
            cursor = finish+gap
        stats.append({'id':scene['id'],'voice_seconds':round(used,3),'tempo_factor':round(speed,3),
                      'last_voice_end':round(cursor-gap,3),'scene_end':scene['end']})
        print(stats[-1], flush=True)
        if cursor-gap > scene['end']-.1:
            raise ValueError(f'Speech overflow: {scene["id"]}')
    peak = float(np.max(np.abs(voice)))
    voice *= .76/max(peak,.01)
    (ROOT/'captions.json').write_text(json.dumps(cues,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'audio-timing.json').write_text(json.dumps({'engine':engine,'voice':CONFIG['voice'] if engine=='edge' else 'Reed (Chinese (China mainland))','scenes':stats},ensure_ascii=False,indent=2)+'\n')
    write_audio(WORK/'narration.wav',voice)
    return voice,cues


def music_bed(voice):
    n=len(voice)
    bed=np.zeros(n,dtype=np.float32)
    beat=60/94
    rng=np.random.default_rng(7)
    def add(at, sound, gain):
        start=int(at*SR)
        end=min(n,start+len(sound))
        if start<n:
            bed[start:end] += gain*sound[:end-start]
    # Original synthesized instrumental: soft kick, muted percussion, bass and minor pads.
    for k in range(int(CONFIG['duration']/beat)+1):
        t=np.arange(int(.22*SR))/SR
        phase=2*np.pi*(48*t+38*.022*(1-np.exp(-t/.022)))
        add(k*beat,np.sin(phase)*np.exp(-t/0.055),.075 if k%4 in (0,2) else .03)
        if k%2:
            t=np.arange(int(.07*SR))/SR
            noise=rng.normal(0,1,len(t))
            noise=np.concatenate(([0],np.diff(noise)))*np.exp(-t/.016)
            add(k*beat,noise,.009)
        t=np.arange(int(.035*SR))/SR
        add((k+.5)*beat,rng.normal(0,1,len(t))*np.exp(-t/.01),.007)
    roots=[146.832,116.541,130.813,110.]
    for k in range(int(CONFIG['duration']/(beat*8))+1):
        root=roots[k%4]
        dur=beat*8
        t=np.arange(int(dur*SR))/SR
        env=np.minimum(t/.35,1)*np.minimum((dur-t)/.6,1)
        pad=sum(np.sin(2*np.pi*root*ratio*t) for ratio in [1,1.189207,1.498307])/3
        add(k*dur,pad*env,.018)
        for b in range(0,8,2):
            tb=np.arange(int(.8*SR))/SR
            bass=(np.sin(2*np.pi*root/2*tb)+.18*np.sin(2*np.pi*root*tb))*np.minimum(tb/.025,1)*np.exp(-tb/.3)
            add(k*dur+b*beat,bass,.04)
    # Detect speech in 20 ms windows, use smooth attack/release gain to keep it dominant.
    block=960
    rms=np.sqrt(np.mean(voice[:n//block*block].reshape(-1,block)**2,axis=1))
    level=1.
    gains=[]
    for value in rms:
        target=.38 if value>.012 else .8
        level+=(target-level)*(.35 if target<level else .05)
        gains.append(level)
    duck=np.interp(np.arange(n),np.arange(len(gains))*block,np.array(gains))
    bed*=duck.astype(np.float32)
    fade=np.minimum(np.arange(n)/SR/1.5,1)*np.minimum((n-np.arange(n))/SR/2,1)
    bed*=fade.astype(np.float32)
    write_audio(WORK/'music.wav',bed)
    stereo=np.column_stack([voice+bed,voice+bed*.96])
    write_audio(WORK/'mix-raw.wav',stereo)
    run(['ffmpeg','-v','error','-y','-i',str(WORK/'mix-raw.wav'),'-af','loudnorm=I=-16:TP=-1.5:LRA=9',
         '-ar',str(SR),str(WORK/'mix.wav')])
    (ROOT/'audio').mkdir(exist_ok=True)
    for name in ['narration','music']:
        run(['ffmpeg','-v','error','-y','-i',str(WORK/f'{name}.wav'),'-c:a','aac','-b:a','160k',str(ROOT/'audio'/f'{name}.m4a')])


def subtitles(cues):
    def stamp(t, separator=','):
        ms=round(t*1000)
        return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02}{separator}{ms%1000:03}'
    srt=[]
    vtt=['WEBVTT','']
    for i,c in enumerate(cues,1):
        srt.extend([str(i),f'{stamp(c["start"])} --> {stamp(c["end"])}',c['text'],''])
        vtt.extend([f'{stamp(c["start"],".")} --> {stamp(c["end"],".")}',c['text'],''])
    (ROOT/'subtitles.srt').write_text('\n'.join(srt))
    (ROOT/'subtitles.vtt').write_text('\n'.join(vtt))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--engine',choices=['edge','say'],default='edge')
    args=parser.parse_args()
    asyncio.run(synthesize(args.engine))
    voice,cues=assemble(args.engine)
    subtitles(cues)
    music_bed(voice)
    print('Audio and timed subtitles ready.',flush=True)

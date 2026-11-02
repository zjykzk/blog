# Harness² 算法执行过程演示

- 成片：`harness2-algorithm-1080p.mp4`（1920×1080，25fps，约 3 分 22 秒，中文配音与字幕）
- 本地播放器：`preview.html`（含章节跳转与字幕轨）
- 旁白稿：`narration.md`；字幕：`subtitles.srt` / `subtitles.vtt`
- 分轨音频：`audio/narration.m4a`、`audio/music.m4a`
- 校验记录：`verification.json`；抽帧：`stills/`、`contact-sheet.jpg`

## 重新生成

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python prepare_audio.py          # 旁白(TTS 需联网)、音乐、时间轴、字幕；离线可加 --engine say
.venv/bin/python render.py --stills 30,60  # 先抽查画面，输出到 frames-check/
.venv/bin/python render.py                 # 渲染成片
```

修改文案只需编辑 `script.json`：`text` 为字幕，`say` 为可选的朗读版本（例如把数字写成读法）。

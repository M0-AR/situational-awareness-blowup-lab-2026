# Recording the 2-minute demo video (optional, recommended for GitHub stars)

GitHub READMEs render GIF inline but not MP4. Best practice (verified 2026 guides):
inline `docs/demo.gif` + link a YouTube video with a clickable thumbnail.

## Option A — use the included clips (30 seconds)
1. `docs/demo.gif` is already embedded in README + preview.html.
2. `docs/demo.mp4` is the same clip with controls in preview.html.
3. Upload `docs/demo.mp4` to YouTube (unlisted is fine), paste the URL into
   README `🎬 Demo video` section and here.

## Option B — record your own terminal (2 minutes)
```bash
# terminal session: run the lab while recording
ffmpeg -f x11grab -s 1280x720 -i :0.0 -r 30 docs/walkthrough.mp4
# in another window:
docker compose up
# then trim + gif:
ffmpeg -y -i docs/walkthrough.mp4 -vf "fps=10,scale=800:-1" docs/demo.gif
```
Narration script (120 seconds):
1. (0:00) "This repo replays a $45B fund losing $35B in days — on live data."
2. (0:20) Run EXP-01, point at July bars (-46% SNDK, +22% ADBE short squeeze).
3. (0:50) Run EXP-02/03: 4x turns +286% into +1145% then -33% into -133%; realized -67% = forced sale.
4. (1:30) Show equity_curve + correlation 0.44→0.81 + 100% bounce.
5. (1:55) "Direction right, survival wrong. docker compose up to verify."

## Thumbnail pattern for README
```markdown
[![Watch the demo](docs/july_drawdown.png)](https://youtube.com/watch?v=PASTE_ID)
```

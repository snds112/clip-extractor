

# Video Clip Extractor (FFmpeg)

A Python script that uses FFmpeg to extract precise clips from video files based on timestamps defined in a CSV file.

## 🚀 Key Features
- Uses FFmpeg for high-performance video cutting
- Supports all video formats that FFmpeg handles
- Preserves original quality with stream copy option
- Lightweight (no Python video processing dependencies)

## 📋 Requirements
- Python 3.6+
- **[FFmpeg](https://ffmpeg.org/)** installed and in system PATH
  - On Windows: `choco install ffmpeg`
  - On Mac: `brew install ffmpeg`
  - On Linux: `sudo apt install ffmpeg`

## 📂 Example Folder Structure
```
videos/                 # Source videos (must match episode numbers)
├── clips/              # Output folder (auto-created)
├── 1.mp4               # Episode 1
├── 2.mov               # Episode 2
└── cuts.csv            # Clip definitions (not necessarily in the video folder)
```
## ⚡ Example Command
```
cd /path/to/video/folder
python /path/to/main.py /path/to/csv
```

## 📝 CSV Format
Required columns:
```csv
episode,name,start time,end time
```

Example (`cuts.csv`):
```csv
episode,name,start time,end time
1,Intro,00:00:05.500,00:00:15.200
2,Action Scene,00:01:30,00:02:45.750
1,Outro,00:10:00,00:11:20
```

### Single Video Mode
To extract all clips from one video:
1. Set all `episode` values to `1` in CSV
2. Place just one video file in the directory

## ⚡ FFmpeg Command
The script generates and executes commands like:
```bash
ffmpeg -n -ss HH:MM:SS -to HH:MM:SS  -i /path/to/video -reset_timestamps 1 -map 0 -c copy -avoid_negative_ts 1 clip_name
```

## 🎬 Output
- Creates `clips/` directory if missing
- Output files: `{episode}_{name}.{original_extension}`
- Preserves:
  - Original video/audio codecs (`-c:v copy -c:a copy`)
  - Metadata
  - Quality

## ⚠️ Notes
1. **FFmpeg must be installed and accessible**
2. Time formats supported:
   - `HH:MM:SS`
   - `HH:MM:SS.milliseconds`
   - `MM:SS`


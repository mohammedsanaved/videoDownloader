# YouTube Video & Playlist Downloader

A Python script for downloading YouTube videos and playlists using yt-dlp with customizable resolution selection.

## Features

- Download single YouTube videos or entire playlists
- Choose from available video resolutions
- Progress tracking with real-time download status
- Robust error handling for failed downloads
- Cross-platform support (Windows, Linux, macOS)
- User-friendly interface with multiple input options

## Prerequisites

### Required Software

1. **Python 3.6 or higher**
2. **FFmpeg** (strongly recommended)
3. **yt-dlp** Python package

## Installation

### Step 1: Install Python

#### Windows

- Download Python from [python.org](https://www.python.org/downloads/)
- During installation, make sure to check "Add Python to PATH"

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Linux (CentOS/RHEL/Fedora)

```bash
# Fedora
sudo dnf install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip
```

### Step 2: Install FFmpeg

#### Windows

**Option 1: Using Chocolatey**

```bash
choco install ffmpeg
```

**Option 2: Using Winget**

```bash
winget install FFmpeg
```

**Option 3: Manual Installation**

1. Download from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract to a folder (e.g., `C:\ffmpeg`)
3. Add the `bin` folder to your system PATH

#### Linux

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install ffmpeg
```

**CentOS/RHEL/Fedora:**

```bash
# Fedora
sudo dnf install ffmpeg

# CentOS/RHEL (enable EPEL first)
sudo yum install epel-release
sudo yum install ffmpeg
```

**Arch Linux:**

```bash
sudo pacman -S ffmpeg
```

### Step 3: Install Python Dependencies

```bash
pip install yt-dlp
```

Or if you're using Python 3 specifically:

```bash
pip3 install yt-dlp
```

### Step 4: Verify Installation

Check if FFmpeg is properly installed:

```bash
ffmpeg -version
```

## Usage

1. **Download the script** and save it as `youtube_downloader.py`

2. **Run the script:**

   ```bash
   python youtube_downloader.py
   ```

   Or on Linux:

   ```bash
   python3 youtube_downloader.py
   ```

3. **Enter a YouTube URL** when prompted:

   - Single video: `https://www.youtube.com/watch?v=VIDEO_ID`
   - Playlist: `https://www.youtube.com/playlist?list=PLAYLIST_ID`

4. **Select resolution:**

   - Choose from the displayed list of available resolutions
   - Enter either the resolution (e.g., `720p`) or the number (e.g., `2`)

5. **Wait for download** to complete. Progress will be displayed in real-time.

## Example Usage

```
Enter the YouTube video URL or Playlist URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ

Fetching available resolutions...

Available resolutions:
1. 1080p
2. 720p
3. 480p
4. 360p

Enter resolution (e.g., '720p') or number (1-4): 2

Starting download in 720p resolution...
Downloading: 45.2% of Rick Astley - Never Gonna Give You Up.mp4 at 1.2MiB/s
✅ Downloaded: Rick Astley - Never Gonna Give You Up.mp4

✅ Download process completed!
```

## File Naming Convention

Downloaded files are saved with the format:

```
[Uploader Name] - [Video Title].[Extension]
```

Example: `Rick Astley - Never Gonna Give You Up.mp4`

## Troubleshooting

### Common Issues

1. **"ffmpeg not found" warning:**

   - Install FFmpeg following the installation instructions above
   - The script will work without FFmpeg but with limited format options

2. **"No module named 'yt_dlp'" error:**

   ```bash
   pip install yt-dlp
   ```

3. **Permission denied errors (Linux):**

   ```bash
   sudo pip3 install yt-dlp
   ```

4. **Downloads failing:**

   - Check your internet connection
   - Verify the YouTube URL is correct and accessible
   - Some videos may be geo-restricted or age-restricted

5. **Python not found (Windows):**
   - Reinstall Python and ensure "Add Python to PATH" is checked
   - Or use the full path: `C:\Python39\python.exe youtube_downloader.py`

### Performance Tips

- For large playlists, ensure you have sufficient disk space
- Close other bandwidth-intensive applications for faster downloads
- Use wired internet connection for more stable downloads

## Script Features

### Error Handling

- Continues downloading other videos if one fails in a playlist
- Provides clear error messages for troubleshooting
- Automatically retries failed connections

### Progress Tracking

- Real-time download progress with percentage and speed
- Clear success/failure indicators
- Estimated time remaining (when available)

### Format Selection

- Automatically selects the best available format for chosen resolution
- Falls back to lower quality if exact resolution isn't available
- Handles different codec availability across playlist videos

## Dependencies

- `yt-dlp`: Modern YouTube downloader library
- `logging`: Built-in Python logging (included)
- `FFmpeg`: External binary for video/audio processing

## License

This script is provided as-is for educational and personal use. Respect YouTube's Terms of Service and copyright laws when downloading content.

## Support

If you encounter issues:

1. Ensure all dependencies are properly installed
2. Check that your URLs are valid and accessible
3. Verify you have sufficient disk space
4. Update yt-dlp: `pip install -U yt-dlp`

For yt-dlp specific issues, refer to the [official documentation](https://github.com/yt-dlp/yt-dlp).

Here's a `README.md` file for your project. This document provides clear instructions to help users access and run the code.

---

# YouTube Playlist and Video Downloader

This Python script allows you to download individual YouTube videos or entire playlists in a resolution of your choice using `yt-dlp`.

## Features

- **Download Resolutions**: Choose your desired resolution (e.g., 1080p, 720p) for all videos in a playlist or a single video.
- **Retry Attempts**: Get up to 3 attempts to enter a valid resolution, with a prompt showing available options.

## Prerequisites

### Installation

Ensure you have Python installed. You can check by running:

```bash
python --version
```

Install `yt-dlp`, which this script uses to handle YouTube downloads:

```bash
pip install yt-dlp
```

## Usage

1. **Clone the Repository** (or download the script directly):

   ```bash
   git clone https://github.com/mohammedsanaved/videoDownloader.git
   cd videoDownloader
   ```

2. **Run the Script**:
   Start the script by executing:

   ```bash
   python highResolution.py
   ```

3. **Input Options**:
   - Enter the URL of the YouTube video or playlist you want to download.
   - Select a resolution from the list of available options (e.g., `720p`, `1080p`).
   - If the resolution you select is not available, you will get up to 3 attempts to enter a valid option.

### Example Walkthrough

1. **Enter the URL**: When prompted, input the YouTube video or playlist URL.

   ```
   Enter the YouTube video URL or Playlist URL: https://www.youtube.com/playlist?list=XXXXXXXXXXX
   ```

2. **Choose Resolution**: The script will display available resolutions for the first video in the playlist.

   ```
   Available resolutions:
   18: 360p
   22: 720p
   137: 1080p
   ```

   Enter the desired resolution format, like `720p` or `1080p`.

3. **Download Progress**: The script will start downloading the video or each video in the playlist with your selected resolution, showing download progress for each.

### Notes

- If the entered resolution is unavailable after 3 attempts, the script will exit.
- Only resolutions available for the video or playlist will work; other formats will show as invalid.

## Troubleshooting

- **KeyError**: If you encounter a `KeyError`, make sure you’re using `webpage_url` in the code for accessing each video in a playlist.
- **Unsupported Resolution**: If your chosen resolution isn’t available, try a different one from the displayed list.

## License

This project is licensed under the MIT License.

---

This guide should provide users with clear steps to install and use your code effectively. Let me know if there's anything specific you’d like to add!

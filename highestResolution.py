from yt_dlp import YoutubeDL

def get_available_resolutions(video_url):
    with YoutubeDL() as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        formats = info_dict.get('formats', [])
        resolutions = {fmt['format_id']: fmt['height'] for fmt in formats if 'height' in fmt}
        return resolutions

def download_video_with_ytdlp(video_url, resolution):
    ydl_opts = {
        'format': f"{resolution}+bestaudio/best",  # Downloads video with best audio
        'progress_hooks': [progress_hook],
        'outtmpl': '%(title)s.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} of {d['filename']} at {d['_speed_str']}")
    elif d['status'] == 'finished':
        print(f"Downloaded: {d['filename']}")

def main():
    video_url = input("Enter the YouTube video URL or Playlist URL: ")
    resolutions = get_available_resolutions(video_url)

    # Display available resolutions
    print("Available resolutions:")
    for fmt, height in resolutions.items():
        print(f"{fmt}: {height}p")

    # Ask the user for the desired resolution
    selected_resolution = input("Enter the resolution (e.g., '1080p', '720p', '480p'): ")

    if selected_resolution in resolutions:
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            if 'entries' in info_dict:  # Check if it's a playlist
                print("Downloading playlist...")
                for entry in info_dict['entries']:
                    print(f"Downloading: {entry['title']}")
                    download_video_with_ytdlp(entry['url'], selected_resolution)
            else:
                download_video_with_ytdlp(video_url, selected_resolution)
    else:
        print("Invalid resolution selected.")

if __name__ == "__main__":
    main()
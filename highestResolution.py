from yt_dlp import YoutubeDL

def get_available_resolutions(video_url):
    with YoutubeDL() as ydl:
        info_dict = ydl.extract_info(video_url, download=False)

        if 'entries' in info_dict:  # Check if it's a playlist
            first_video = info_dict['entries'][0]
            video_formats = first_video.get('formats', [])
            resolutions = {fmt['format_id']: f"{fmt['height']}p" for fmt in video_formats if 'height' in fmt}
        else:
            formats = info_dict.get('formats', [])
            resolutions = {fmt['format_id']: f"{fmt['height']}p" for fmt in formats if 'height' in fmt}
        
        return resolutions

def download_video_with_ytdlp(video_url, format_id):
    ydl_opts = {
        'format': f"{format_id}+bestaudio/best",
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
    for fmt, height in sorted(resolutions.items(), key=lambda x: x[1], reverse=True):
        print(f"{fmt}: {height}")

    # Ask the user for the desired resolution with up to 3 attempts
    attempts = 3
    selected_format = None

    while attempts > 0:
        selected_resolution = input("Enter the resolution (e.g., '720p', '1080p', '480p'): ")
        
        # Find matching format_id for the resolution
        selected_format = next((fmt for fmt, height in resolutions.items() if height == selected_resolution), None)
        
        if selected_format:
            break  # Exit the loop if a valid resolution is selected
        else:
            attempts -= 1
            print(f"Invalid resolution selected. You have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.")
            if attempts > 0:
                print("Please enter one of the available resolutions shown above.")

    if selected_format:
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            if 'entries' in info_dict:  # Check if it's a playlist
                print("Downloading playlist...")
                for entry in info_dict['entries']:
                    print(f"Downloading: {entry['title']}")
                    download_video_with_ytdlp(entry['webpage_url'], selected_format)
            else:
                download_video_with_ytdlp(video_url, selected_format)
    else:
        print("Too many invalid attempts. Exiting the program.")

if __name__ == "__main__":
    main()

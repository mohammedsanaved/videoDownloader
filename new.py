from yt_dlp import YoutubeDL
import logging

# Set up logger for debugging (optional)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_available_resolutions(video_url):
    ydl_opts = {
        'no_proxy': True,
        'logger': logger,
        'proxy': None,
        'verbose': True,
        'quiet': False,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            if 'entries' in info_dict:  # Playlist
                # Get resolutions from first few videos to show common formats
                all_resolutions = set()
                for i, entry in enumerate(info_dict['entries'][:3]):  # Check first 3 videos
                    if entry:  # Skip None entries
                        formats = entry.get('formats', [])
                        video_formats = [fmt for fmt in formats if fmt.get('height')]
                        for fmt in video_formats:
                            if fmt.get('height'):
                                all_resolutions.add(f"{fmt['height']}p")
                
                return sorted(list(all_resolutions), key=lambda x: int(x.replace('p', '')), reverse=True)
            else:
                formats = info_dict.get('formats', [])
                resolutions = []
                for fmt in formats:
                    if fmt.get('height'):
                        res = f"{fmt['height']}p"
                        if res not in resolutions:
                            resolutions.append(res)
                
                return sorted(resolutions, key=lambda x: int(x.replace('p', '')), reverse=True)
    except Exception as e:
        print(f"Error getting resolutions: {e}")
        return []

def download_content(video_url, resolution):
    # Use height-based format selection instead of format_id
    format_selector = f"best[height<={resolution.replace('p', '')}]/best"
    
    ydl_opts = {
        'no_proxy': True,
        'format': format_selector,
        'progress_hooks': [progress_hook],
        'outtmpl': '%(uploader)s - %(title)s.%(ext)s',
        'logger': logger,
        'verbose': False,  # Reduce verbosity for cleaner output
        'ignoreerrors': True,  # Continue on errors
        'no_warnings': False,
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            if 'entries' in info_dict:  # Playlist
                print(f"Downloading playlist: {info_dict.get('title', 'Unknown')}")
                print(f"Total videos: {len([e for e in info_dict['entries'] if e])}")
                
                # Download all videos in playlist
                ydl.download([video_url])
            else:
                print(f"Downloading single video: {info_dict.get('title', 'Unknown')}")
                ydl.download([video_url])
                
    except Exception as e:
        print(f"Download failed: {e}")

def progress_hook(d):
    if d['status'] == 'downloading':
        filename = d.get('filename', 'Unknown')
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        print(f"Downloading: {percent} of {filename} at {speed}")
    elif d['status'] == 'finished':
        print(f"✅ Downloaded: {d.get('filename', 'Unknown')}")
    elif d['status'] == 'error':
        print(f"❌ Error downloading: {d.get('filename', 'Unknown')}")

def main():
    video_url = input("Enter the YouTube video URL or Playlist URL: ").strip()
    
    if not video_url:
        print("No URL provided. Exiting.")
        return
    
    print("Fetching available resolutions...")
    resolutions = get_available_resolutions(video_url)
    
    if not resolutions:
        print("Could not fetch available resolutions. Exiting.")
        return
    
    # Display available resolutions
    print("\nAvailable resolutions:")
    for i, res in enumerate(resolutions, 1):
        print(f"{i}. {res}")
    
    # Ask the user for the desired resolution
    attempts = 3
    selected_resolution = None
    
    while attempts > 0:
        try:
            choice = input(f"\nEnter resolution (e.g., '720p') or number (1-{len(resolutions)}): ").strip()
            
            # Try to parse as number first
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(resolutions):
                    selected_resolution = resolutions[idx]
                    break
            
            # Try to find exact match
            if choice in resolutions:
                selected_resolution = choice
                break
            
            # Try to find partial match
            matches = [res for res in resolutions if choice in res]
            if len(matches) == 1:
                selected_resolution = matches[0]
                break
            elif len(matches) > 1:
                print(f"Multiple matches found: {matches}. Please be more specific.")
            else:
                print("Invalid selection.")
            
        except ValueError:
            print("Invalid input.")
        
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.")
    
    if selected_resolution:
        print(f"\nStarting download in {selected_resolution} resolution...")
        download_content(video_url, selected_resolution)
        print("\n✅ Download process completed!")
    else:
        print("Too many invalid attempts. Exiting the program.")

if __name__ == "__main__":
    main()

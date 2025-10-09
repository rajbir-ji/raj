import yt_dlp

# Prompt user for YouTube URL
url = input("Enter YouTube URL: ")

# Prompt user for format choice
format_choice = input("Enter format (MP3 or MP4): ").strip().upper()

if format_choice == 'MP3':
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
elif format_choice == 'MP4':
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
    }
else:
    print("Invalid format. Please choose MP3 or MP4.")
    exit(1)

# Download the video/audio
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")

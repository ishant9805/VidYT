from pytube import YouTube

def download_media(video_url):
    try:
        # Create a YouTube object
        youtube_video = YouTube(video_url)

        # Download the media to the specified output path
        # print(f"Downloading {media_type}: {youtube_video.title}...")
        # media_stream.download(output_path)
        # print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")



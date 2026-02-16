# EN: YouTube Video Downloader with Progress Bar
# AZ: Yüklənmə faizini göstərən YouTube Video Yükləyici

from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_video(url):
    try:
        # EN: Initialize YouTube object and show progress
        # AZ: YouTube obyektini yaradır və yüklənmə gedişatını göstərir
        yt = YouTube(url, on_progress_callback=on_progress)
        
        print(f"\nTitle / Ad: {yt.title}")
        print(f"Views / Baxış sayı: {yt.views}")

        # EN: Filter for the highest resolution MP4 stream
        # AZ: Ən yüksək keyfiyyətli MP4 formatını seçir
        stream = yt.streams.get_highest_resolution()
        
        print("Downloading... / Yüklənir...")
        stream.download()
        print("\n✅ Download Complete! / Yükləmə tamamlandı!")
        
    except Exception as e:
        print(f"❌ Error / Xəta: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube Link / YouTube linkini daxil edin: ")
    download_video(video_url)

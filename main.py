from pytube import YouTube
import os

url = input("Enter the URL of video: ")

class VideoDownloader:
    def __init__(self, url):
        try:
            self.video = YouTube(url)
        
        except Exception as e:
            print("Error.", e)
            self.video = None

    def show_info(self):
        if self.video is None:
            print("امکان دانلود وجود ندارد.")
            return
        
        print("Title: ", self.video.title)
        print("Length: ", self.video.length)
        print("Thumbnail: ", self.video.thumbnail_url)

        filtered_streams = self.video.streams.filter(progressive=True)
        audio_streams = self.video.streams.filter(only_audio= True)

        print("\nVideo + Audio Streams: ")
        for i, stream in enumerate(filtered_streams):
            print(f"{i}: {stream}")

        print("\nAudio-only Streams: ")
        for i, stream in enumerate(audio_streams):
            print(f"{i + len(filtered_streams)}: {stream}")

        self.filtered_streams = list(filtered_streams) + list(audio_streams)

    def download_video(self):
        if self.video is None:
            print("امکان دانلود وجود ندارد.")
            return
        
        download_path = input("Enter folder to save video(default: Downloads): ")
        if download_path.strip() == "":
            download_path = "Downloads"
        
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        try:
            number = int(input("Enter the number of stream you want to download: "))
            self.filtered_streams[number].download(output_path = download_path)
            print("Download Success.")
        except ValueError:
            print("یک عدد وارد کنید")
        
        except IndexError:
            print("شماره انتخابی معتبر نیست.")
        
        except Exception as e:
            print("خطا در دانلود", e)
        


video = VideoDownloader(url)
video.show_info()
video.download_video
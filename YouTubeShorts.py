import pytube
from pytube import YouTube

url = ''

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

download_path = './'

stream.download(output_path=download_path)

print(f"Downloaded '{yt.title}' to {download_path}")
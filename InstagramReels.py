import requests

video_url = ''

download_path = 'downloaded_reel.mp4'

response = requests.get(video_url, stream=True)

if response.status_code == 200:
    with open(download_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk: 
                file.write(chunk)
    print(f"Video downloaded successfully and saved at {download_path}")
else:
    print(f"Failed to download video. Status code: {response.status_code}")
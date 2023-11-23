import requests
import yt_dlp


def download_video(video_url):
    ydl_opts = {
        'ffmpeg_location': './ffmpeg',
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url)
        return info_dict


def upload_video(name):
    headers = {'Content-Type': 'application/octet-stream'}
    with open(name, 'rb') as file:
        file_content = file.read()
    url = f'http://router.wxioi.fun:4002/api/v1/fs/mnt/fs/Data/Video/{name}'
    return requests.put(url, data=file_content, headers=headers)

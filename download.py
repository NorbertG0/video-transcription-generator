import yt_dlp

def download_clip(url):
    options = {
        "outtmpl": "%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)

        file_name = ydl.prepare_filename(info)


    return file_name

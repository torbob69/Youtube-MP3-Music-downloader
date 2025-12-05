# download required modules (in your own virtual environment) and ffmpeg

from yt_dlp import YoutubeDL
from googleapiclient.discovery import build

API_KEY = "your api key here"

def search_video(query):
    try:
        youtube = build("youtube", "v3", developerKey=API_KEY)
        req = youtube.search().list(
            part="id",
            q=query,
            maxResults=1,
            type="video"
        )
        res = req.execute()

        if len(res["items"]) == 0:
            return None

        video_id = res["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"

    except Exception as e:
        print("Search failed:", e)
        return None


def download_mp3(urls, path):
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": path + "/%(title)s.%(ext)s",
            "ffmpeg_location": r"C:\ffmpeg\bin",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }


        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)

        print("Success download")

    except Exception as e:
        print("Download failed:", e)


path = input("download path: ")

urls = []

confirm = input("autocollect from txt file/no? [y/n]: ")
if confirm == 'y' :
    with open("txturl.txt", "r") as read:
        print("opening file...")
        for line in read:
            print(line.strip())
            url = search_video(line.split())
            print("Found:", url)
            urls.append(url)
elif confirm == 'n':
    while True:
        q = input("Search video (or 'n' to stop): ")
        if q == "n":
            break

        url = search_video(q)
        if url:
            print("Found:", url)
            urls.append(url)
        else:
            print("No result.")

print("Collected URLs:", urls)

if len(urls) > 0:
    download_mp3(urls, path)
else:
    print("No videos to download.")

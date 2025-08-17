import yt_dlp
import os
import json

# Path to your Google OAuth JSON file
OAUTH_JSON_FILE = "google_oauth.json"

with open(OAUTH_JSON_FILE, "r") as f:
    creds = json.load(f)
OAUTH_CLIENT_ID = creds["installed"]["client_id"]
OAUTH_CLIENT_SECRET = creds["installed"]["client_secret"]

def download(url, out_dir):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(out_dir, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "youtube_include_oauth2_token": True,
        "oauth2_client_id": OAUTH_CLIENT_ID,
        "oauth2_client_secret": OAUTH_CLIENT_SECRET,
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        filename = os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3"
        return filename

import yt_dlp
import os
import json

OAUTH_JSON_FILE = "google_oauth.json"

with open(OAUTH_JSON_FILE, "r") as f:
    creds = json.load(f)
OAUTH_CLIENT_ID = creds["installed"]["client_id"]
OAUTH_CLIENT_SECRET = creds["installed"]["client_secret"]

def download(url, out_dir="downloads"):
    os.makedirs(out_dir, exist_ok=True)

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(out_dir, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "youtube_include_oauth2_token": True,
        "oauth2_client_id": OAUTH_CLIENT_ID,
        "oauth2_client_secret": OAUTH_CLIENT_SECRET,
        "merge_output_format": "mp4",
        "postprocessor_args": [
            "-c:v", "copy",        # copy video stream
            "-c:a", "aac",         # convert audio to AAC
            "-b:a", "192k"         # audio bitrate
        ],
        "progress_hooks": [lambda d: print(f"Status: {d['status']}") if 'status' in d else None]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        filename = ydl.prepare_filename(info)
        if not filename.endswith(".mp4"):
            filename = os.path.splitext(filename)[0] + ".mp4"
        print(f"Downloaded to: {filename}")
        return filename

if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()
    out_dir = input("Enter output folder (default 'downloads'): ").strip() or "downloads"
    download(url, out_dir)

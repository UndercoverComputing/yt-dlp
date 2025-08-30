import yt_dlp
import os
import json

# Path to your Google OAuth JSON file
OAUTH_JSON_FILE = "google_oauth.json"

with open(OAUTH_JSON_FILE, "r") as f:
    creds = json.load(f)
OAUTH_CLIENT_ID = creds["installed"]["client_id"]
OAUTH_CLIENT_SECRET = creds["installed"]["client_secret"]

def download(url, out_dir="downloads", progress_hook=None):
    os.makedirs(out_dir, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(out_dir, "%(title)s.%(ext)s"),
        "noplaylist": False,  # allow full playlists
        "youtube_include_oauth2_token": True,
        "oauth2_client_id": OAUTH_CLIENT_ID,
        "oauth2_client_secret": OAUTH_CLIENT_SECRET,
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ],
    }
    if progress_hook:
        ydl_opts["progress_hooks"] = [progress_hook]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filenames = []
        playlist_title = None

        if "entries" in info:  # Playlist
            playlist_title = info.get("title", "playlist")
            for entry in info["entries"]:
                if not entry:
                    continue
                filenames.append(os.path.splitext(ydl.prepare_filename(entry))[0] + ".mp3")
        else:  # Single video
            filenames.append(os.path.splitext(ydl.prepare_filename(info))[0] + ".mp3")

        return filenames, playlist_title

if __name__ == "__main__":
    url = input("Enter YouTube URL (video or playlist): ").strip()
    out_dir = input("Enter output folder (default 'downloads'): ").strip() or "downloads"
    files, title = download(url, out_dir)
    if title:
        print(f"Downloaded playlist: {title}")
    print("Downloaded files:")
    for f in files:
        print(" -", f)

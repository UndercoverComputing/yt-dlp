import yt_dlp
import os
import json

# Path to your Google OAuth JSON file
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
        "noplaylist": False,  # allow full playlists
        "youtube_include_oauth2_token": True,
        "oauth2_client_id": OAUTH_CLIENT_ID,
        "oauth2_client_secret": OAUTH_CLIENT_SECRET,
        "merge_output_format": "mp4",
        "postprocessor_args": [
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k"
        ],
        "progress_hooks": [lambda d: print(f"Status: {d['status']}") if 'status' in d else None]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filenames = []
        playlist_title = None

        if "entries" in info:  # Playlist
            playlist_title = info.get("title", "playlist")
            for entry in info["entries"]:
                if not entry:
                    continue
                fname = ydl.prepare_filename(entry)
                if not fname.endswith(".mp4"):
                    fname = os.path.splitext(fname)[0] + ".mp4"
                filenames.append(fname)
        else:  # Single video
            fname = ydl.prepare_filename(info)
            if not fname.endswith(".mp4"):
                fname = os.path.splitext(fname)[0] + ".mp4"
            filenames.append(fname)

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
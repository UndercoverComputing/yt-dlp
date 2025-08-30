# YouTube Downloader

A simple Flask-based web application to download YouTube videos as MP4 or MP3 files. The application uses `yt_dlp` for downloading and processing media and includes a cleanup mechanism to remove downloaded files older than 10 minutes.

## Features
- Download YouTube videos as MP4 (video + audio).
- Download YouTube audio as MP3.
- Automatically deletes downloaded files after 10 minutes to manage disk space.
- Simple web interface for entering YouTube URLs and selecting download format.
- Run as docker container
- Run as python script

## Installation

### Set Up Google Cloud Credentials

Google Cloud credentials are required to download age-restricted or private YouTube content.

1. Go to [Google Cloud Console → APIs & Services → Credentials](https://console.cloud.google.com/apis/credentials).
2. Create an OAuth client ID:

   * **Application type**: Desktop app
   * **Name**: Choose a name (e.g., `yt-dlp-server`)
3. Download the JSON credentials file.
4. Save the JSON file as `google_oauth.json` in the root directory of the project and ensure the path matches what is used in `mp4.py` and `mp3.py`.

### Docker:

Refer to [docker/README.md](https://github.com/UndercoverComputing/yt-dlp/blob/main/docker/README.md)

### Python:

Refer to [python/README.md](https://github.com/UndercoverComputing/yt-dlp/blob/main/python/README.md)

### Windows

Refer to [windows/README.md](https://github.com/UndercoverComputing/yt-dlp/blob/main/windows/README.md)

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.
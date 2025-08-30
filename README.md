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

### Docker:

Refer to [docker/README.md](https://github.com/UndercoverComputing/yt-dlp/blob/main/docker/README.md)

### Python:

Refer to [python/README.md](https://github.com/UndercoverComputing/yt-dlp/blob/main/python/README.md)

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.
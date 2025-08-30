# YouTube Downloader

A simple Flask-based web application to download YouTube videos as MP4 or MP3 files. The application uses `yt_dlp` for downloading and processing media and includes a cleanup mechanism to remove downloaded files older than 10 minutes.

## Features
- Download YouTube videos as MP4 (video + audio).
- Download YouTube audio as MP3.
- Automatically deletes downloaded files after 10 minutes to manage disk space.
- Simple web interface for entering YouTube URLs and selecting download format.

## Prerequisites

* [Docker](https://www.docker.com/get-started) installed on your system
* [Docker Compose](https://docs.docker.com/compose/install/) installed
* Git installed to clone the repository

### Project Structure
Ensure your project directory contains the following files:
```
yt-dlp/docker
├── Dockerfile           # Docker image definition
├── app.py               # Main Flask application
├── mp4.py               # MP4 download logic
├── mp3.py               # MP3 download logic
├── templates/
│   └── index.html       # Web interface
├── downloads/           # Directory for downloaded files (auto-created)
└── google_oauth.json    # Google Cloud credentials (optional)
```

## Installation

1. Clone the Repository
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/UndercoverComputing/yt-dlp
   cd yt-dlp
   ```

2. Set Up Google Cloud Credentials
   If you need to download age-restricted or private YouTube content, you may need Google Cloud credentials for authentication.
   
   1. Go to [Google Cloud Console → APIs & Services → Credentials](https://console.cloud.google.com/apis/credentials).
   2. Create an OAuth client ID:
      - **Application type**: Desktop app
      - **Name**: Choose a name (e.g., `yt-dlp-server`)
   3. Download the JSON credentials file.
   4. Save the JSON file as `google_oauth.json` in the root directory of the project. Alternatively, modify the `OAUTH_JSON_FILE` path in `mp4.py` and `mp3.py` to point to your credentials file.
   
   **Note**: The `google_oauth.json` file is referenced in the `yt_dlp` configuration in `mp4.py` and `mp3.py`. Ensure it is correctly placed or update the file path in the code if needed.

3. **Run the Application**

   Build and start the Docker containers in detached mode:

   ```bash
   docker build -t yt-dlp:1.3 .
   docker run -d --name yt-dlp -p 8000:8000 -v /opt/yt-dlp/downloads:/downloads  yt-dlp:1.3
   ```


## Usage

1. Open your browser and navigate to `http://localhost:8000`.

2. Enter a YouTube video URL and select either "Download MP4" or "Download MP3".

3. The file will download automatically, and files older than 10 minutes will be deleted from the `downloads` directory. Please do not close the browser tab while it loads the download.

## Notes
- The application uses `yt_dlp` to handle YouTube downloads, which supports a wide range of formats and options. You can modify the `ydl_opts` in `mp4.py` or `mp3.py` to customize download settings (e.g., video quality, audio bitrate).
- The cleanup mechanism runs on every page load, removing files in the `downloads` directory older than 10 minutes.
- Ensure `google_oauth.json` is present if downloading content that requires authentication (e.g., age-restricted videos).

## Troubleshooting
* Download fails: Verify the YouTube URL is valid and that `google_oauth.json` is correctly configured for restricted content.
* Check Docker logs for errors: `docker compose logs yt-dlp`.
* Ensure Docker and Docker Compose are up to date.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.

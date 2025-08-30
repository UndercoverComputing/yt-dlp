# YouTube Downloader

A simple Flask-based web application to download YouTube videos as MP4 or MP3 files. The application uses `yt_dlp` for downloading and processing media and includes a cleanup mechanism to remove downloaded files older than 10 minutes.

## Features

* Download YouTube videos as MP4 (video + audio).
* Download YouTube audio as MP3.
* Automatically deletes downloaded files after 10 minutes to manage disk space.
* Simple web interface for entering YouTube URLs and selecting download format.

## Prerequisites

* Python 3.6 or higher
* pip (Python package manager)
* Google Cloud credentials for authentication (required for age-restricted or private content)
* FFmpeg installed on your system (required by `yt_dlp` for media processing)

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/UndercoverComputing/yt-dlp
cd yt-dlp/python
```

### 2. Install Python & Dependencies

Install the required Python packages using pip:

```bash
sudo apt update
sudo apt install python3 python3-pip python3.11-venv -y 
python3 -m venv env
source env/bin/activate
pip install flask yt_dlp
```

### 3. Install FFmpeg

FFmpeg is required for `yt_dlp` to merge video/audio and convert formats.

```bash
sudo apt install ffmpeg
```

### 4. Set Up Google Cloud Credentials

Google Cloud credentials are required to download age-restricted or private YouTube content.

1. Go to [Google Cloud Console → APIs & Services → Credentials](https://console.cloud.google.com/apis/credentials).
2. Create an OAuth client ID:

   * **Application type**: Desktop app
   * **Name**: Choose a name (e.g., `yt-dlp-server`)
3. Download the JSON credentials file.
4. Save the JSON file as `google_oauth.json` in the root directory of the project and ensure the path matches what is used in `mp4.py` and `mp3.py`.

### 5. Project Structure

Ensure your project directory contains the following files:

```
yt-dlp/python
├── app.py               # Main Flask application
├── mp4.py               # MP4 download logic
├── mp3.py               # MP3 download logic
├── templates/
│   └── index.html       # Web interface
├── downloads/           # Directory for downloaded files (auto-created)
└── google_oauth.json    # Google Cloud credentials
```

## Usage

1. Run the Flask application:

   ```bash
   python3 app.py
   ```

   The server will start on `http://0.0.0.0:8000` in debug mode.

2. Open your browser and navigate to `http://localhost:8000`.

3. Enter a YouTube video URL and select either "Download MP4" or "Download MP3".

4. The file will download automatically, and files older than 10 minutes will be deleted from the `downloads` directory.

## Notes

* The application uses `yt_dlp` to handle YouTube downloads, which supports a wide range of formats and options. You can modify the `ydl_opts` in `mp4.py` or `mp3.py` to customize download settings (e.g., video quality, audio bitrate).
* The cleanup mechanism runs on every page load, removing files in the `downloads` directory older than 10 minutes.
* Ensure `google_oauth.json` is correctly configured to access restricted content.

## Troubleshooting

* **FFmpeg not found**: Ensure FFmpeg is installed and added to your system PATH.
* **Download fails**: Verify the YouTube URL is valid and that `google_oauth.json` is correctly configured for restricted content.
* **Port conflicts**: If port 8000 is in use, modify the `port` parameter in `app.py` (e.g., `app.run(host="0.0.0.0", port=8080, debug=True)`).
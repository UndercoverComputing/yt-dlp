# YouTube Downloader

A simple Flask-based web application to download YouTube videos as MP4 or MP3 files. The application uses `yt_dlp` for downloading and processing media and includes a cleanup mechanism to remove downloaded files older than 10 minutes.

## Features

* Download YouTube videos as MP4 (video + audio).
* Download YouTube audio as MP3.
* Automatically deletes downloaded files after 10 minutes to manage disk space.
* Simple web interface for entering YouTube URLs and selecting download format.

## Install

1. Download the [latest release](https://github.com/UndercoverComputing/yt-dlp/releases) for windows and extract the folder.
2. Place your Google Cloud Credentials json in the same folder, and name it `google_oauth.json`.
3. Install ffmpeg: https://www.wikihow.com/Install-FFmpeg-on-Windows
4. Run yt-dlp.exe
5. Downloads will go to the folder `downloads` which is created in the same directory as the .exe

**(At this stage you will have to use the terminal output to see when the download is complete)**

## Build

1. Clone the Repository
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/UndercoverComputing/yt-dlp
   cd yt-dlp/windows
   ```

2. Install prerequisites

   ```shell
   pip install pywebview flask pyinstaller yt-dlp
   ```

3. Build the application

   ```shell
   pyinstaller --onefile --add-data "templates;templates" main.py
   ```

2. Place your Google Cloud Credentials json in the same folder, and name it `google_oauth.json`.
3. Run yt-dlp.exe

## Notes

* The application uses `yt_dlp` to handle YouTube downloads, which supports a wide range of formats and options. You can modify the `ydl_opts` in `mp4.py` or `mp3.py` to customize download settings (e.g., video quality, audio bitrate).
* The cleanup mechanism runs on every page load, removing files in the `downloads` directory older than 10 minutes.
* Ensure `google_oauth.json` is correctly configured to access restricted content.

## Troubleshooting

* FFmpeg not found: Ensure FFmpeg is installed and added to your system PATH.
* Download fails: Verify the YouTube URL is valid and that `google_oauth.json` is correctly configured for restricted content.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.

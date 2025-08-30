from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import time
import mp4
import mp3

app = Flask(__name__)
CACHE_DIR = "downloads"
os.makedirs(CACHE_DIR, exist_ok=True)

# Clean up files older than 10 minutes
def cleanup_cache():
    now = time.time()
    for f in os.listdir(CACHE_DIR):
        file_path = os.path.join(CACHE_DIR, f)
        if os.path.isfile(file_path) and now - os.path.getmtime(file_path) > 600:
            os.remove(file_path)

@app.route("/", methods=["GET", "POST"])
def index():
    cleanup_cache()
    if request.method == "POST":
        youtube_url = request.form.get("youtube_url")
        if "mp4" in request.form:
            out_files, playlist_title = mp4.download(youtube_url, CACHE_DIR)
        elif "mp3" in request.form:
            out_files, playlist_title = mp3.download(youtube_url, CACHE_DIR)
        else:
            return redirect(url_for("index"))

        # If multiple files -> zip them
        if len(out_files) > 1:
            import zipfile, io
            # Use playlist title if available
            zip_name = playlist_title or "playlist"
            safe_name = "".join(c if c.isalnum() or c in " -_()" else "_" for c in zip_name)

            zip_buf = io.BytesIO()
            with zipfile.ZipFile(zip_buf, "w") as zipf:
                for f in out_files:
                    zipf.write(f, os.path.basename(f))
            zip_buf.seek(0)
            return send_file(
                zip_buf,
                as_attachment=True,
                download_name=f"{safe_name}.zip",
                mimetype="application/zip"
            )
        else:
            return send_file(out_files[0], as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

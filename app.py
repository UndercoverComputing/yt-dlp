import os
import time
import traceback

# Path to your Google credentials file
GOOGLE_CREDENTIALS = "google-credentials.json"

def freeze_on_error(msg, exc=None):
    """Prints error and freezes until user presses Enter."""
    if exc:
        traceback.print_exc()
    print("\n--- ERROR ---")
    print(msg)
    print("Press Enter to exit...")
    input()
    raise SystemExit(1)

try:
    from flask import Flask, render_template, request, send_file, redirect, url_for
    import mp4
    import mp3
except Exception as e:
    freeze_on_error("Startup failed: missing dependency or import error.", e)

# Check if Google JSON file exists
if not os.path.isfile(GOOGLE_CREDENTIALS):
    freeze_on_error(f"Google credentials file not found: {GOOGLE_CREDENTIALS}")

app = Flask(__name__)
CACHE_DIR = "downloads"
os.makedirs(CACHE_DIR, exist_ok=True)

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
        try:
            if "mp4" in request.form:
                out_files, playlist_title = mp4.download(youtube_url, CACHE_DIR)
            elif "mp3" in request.form:
                out_files, playlist_title = mp3.download(youtube_url, CACHE_DIR)
            else:
                return redirect(url_for("index"))

            if len(out_files) > 1:
                import zipfile, io
                zip_name = playlist_title or "playlist"
                safe_name = "".join(
                    c if c.isalnum() or c in " -_()" else "_" for c in zip_name
                )
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

        except Exception as e:
            freeze_on_error("Request handling failed.", e)
            return "An error occurred. Check the terminal.", 500

    return render_template("index.html")

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8000, debug=True)
    except Exception as e:
        freeze_on_error("Flask failed to start.", e)

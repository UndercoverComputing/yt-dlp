import os
import sys
import time
import traceback
from flask import Flask, render_template, request, send_file, redirect, url_for
import mp4
import mp3

# --- Path helpers ---
if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
    template_folder = os.path.join(sys._MEIPASS, "templates")  # bundled in EXE
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    template_folder = os.path.join(exe_dir, "templates")

CACHE_DIR = os.path.join(exe_dir, "downloads")
os.makedirs(CACHE_DIR, exist_ok=True)

# --- Check Google OAuth JSON ---
GOOGLE_CREDENTIALS = os.path.join(exe_dir, "google_oauth.json")
if not os.path.isfile(GOOGLE_CREDENTIALS):
    print(f"ERROR: Google credentials file not found: {GOOGLE_CREDENTIALS}")
    input("Press Enter to exit...")
    raise SystemExit(1)

# --- Flask app ---
app = Flask(__name__, template_folder=template_folder)

def freeze_on_error(msg, exc=None):
    """Prints error and freezes until user presses Enter."""
    if exc:
        traceback.print_exc()
    print("\n--- ERROR ---")
    print(msg)
    print("Press Enter to exit...")
    input()
    raise SystemExit(1)

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
        app.run(host="127.0.0.1", port=8000, debug=False, use_reloader=False)
    except Exception as e:
        freeze_on_error("Flask failed to start.", e)
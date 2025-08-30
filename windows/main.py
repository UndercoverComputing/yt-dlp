import threading
import sys
import os
import webview
from app import app, freeze_on_error

# Determine folder of the EXE/script
if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))

# Function to start Flask
def start_flask():
    try:
        app.run(host="127.0.0.1", port=8000, debug=False, use_reloader=False)
    except Exception as e:
        freeze_on_error("Flask failed to start.", e)

if __name__ == "__main__":
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Wait a moment to let Flask start
    import time
    time.sleep(1)

    # Open a PyWebView window pointing to the local Flask server
    try:
        webview.create_window(
            "YouTube Downloader",
            "http://127.0.0.1:8000",
            width=500,
            height=400,
            resizable=False
        )
        webview.start()
    except Exception as e:
        freeze_on_error("Failed to open the application window.", e)
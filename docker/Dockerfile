FROM python:3.11-slim

# Install ffmpeg and cleanup to keep image small
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy application code
COPY app.py mp3.py mp4.py requirements.txt templates/ ./

# Install python deps
RUN pip install --no-cache-dir -r requirements.txt

# Make sure downloads dir exists
RUN mkdir -p /downloads

# Set environment so yt-dlp knows where to drop files
ENV CACHE_DIR=/downloads

# Expose flask port
EXPOSE 8000

# Run app
CMD ["python", "app.py"]

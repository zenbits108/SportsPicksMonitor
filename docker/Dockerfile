FROM python:3.12-slim

# system deps for Tesseract + image libs
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        tesseract-ocr libtesseract-dev libleptonica-dev \
        ffmpeg libsm6 libxext6 git && \
    rm -rf /var/lib/apt/lists/*

# create working dir
WORKDIR /app

# copy code and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["/entrypoint.sh"]

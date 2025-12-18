FROM python:3.9.7-slim-buster

WORKDIR /bot

ENV DEBIAN_FRONTEND=noninteractive

RUN echo "deb http://archive.debian.org/debian buster main" > /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian-security buster/updates main" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    wget \
    pv \
    jq \
    python3-dev \
    mediainfo \
    ca-certificates \
    xz-utils && \
    rm -rf /var/lib/apt/lists/*

RUN wget -O ffmpeg.tar.xz https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz && \
    tar -xJf ffmpeg.tar.xz && \
    mv ffmpeg-master-latest-linux64-gpl/bin/ffmpeg /usr/local/bin/ffmpeg && \
    mv ffmpeg-master-latest-linux64-gpl/bin/ffprobe /usr/local/bin/ffprobe && \
    chmod +x /usr/local/bin/ffmpeg /usr/local/bin/ffprobe && \
    rm -rf ffmpeg.tar.xz ffmpeg-master-latest-linux64-gpl

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod +x run.sh

CMD ["bash", "run.sh"]

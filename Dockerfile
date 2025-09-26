FROM python:3.9.7-slim-buster

# Create and set working directory
WORKDIR /bot

# Set environment variable for non-interactive apt
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install dependencies in one layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    wget \
    pv \
    jq \
    python3-dev \
    ffmpeg \
    mediainfo && \
    rm -rf /var/lib/apt/lists/*

# Copy application files
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set executable permissions for run.sh (if needed)
RUN chmod +x run.sh

# Specify the command to run
CMD ["bash", "run.sh"]

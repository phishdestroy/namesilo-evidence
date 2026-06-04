FROM python:3.11-slim

WORKDIR /app

# Install system deps for aiodns/aiohttp
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY handler.py fingerprint.py local_scan.py ./

ENV HTTP_TIMEOUT=5
ENV MAX_REDIRECTS=3
ENV CONCURRENCY=400
ENV CHUNK_SIZE=2000

CMD ["python3", "local_scan.py"]

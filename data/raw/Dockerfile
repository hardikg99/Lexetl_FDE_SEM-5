FROM apache/airflow:3.1.1

USER root
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    libgl1 \
    build-essential \
    python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# ✅ Install NLTK models at build time
RUN python3 -m nltk.downloader punkt punkt_tab

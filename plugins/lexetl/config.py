import os

BASE_DIR = "/opt/airflow"

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")
COLLECTION_NAME = "legal_docs"   # ✅ Required by store.py

EMBEDDING_MODEL_NAME = "all-mpnet-base-v2"

import os

BASE_DIR = "/opt/airflow"

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")
COLLECTION_NAME = "legal_docs"

# ✅ MiniLM = fast & lightweight
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

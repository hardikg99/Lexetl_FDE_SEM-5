import os
from chromadb import PersistentClient
from lexetl.config import CHROMA_DB_DIR, COLLECTION_NAME


def init_chroma():
    """Initialize Chroma DB client and collection, creating if not exist."""
    os.makedirs(CHROMA_DB_DIR, exist_ok=True)
    client = PersistentClient(path=CHROMA_DB_DIR)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def store_embeddings(texts, embeddings, metadatas, ids):
    """Insert or update embeddings inside Chroma."""
    if not embeddings:
        raise ValueError("❌ No embeddings received — cannot store empty data.")

    collection = init_chroma()
    collection.upsert(
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )
    return f"✅ Stored {len(ids)} vectors into Chroma"
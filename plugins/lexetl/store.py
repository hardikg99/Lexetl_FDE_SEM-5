import os
from chromadb import PersistentClient
from lexetl.config import CHROMA_DB_DIR, COLLECTION_NAME


def init_chroma():
    """Initialize Chroma DB client and collection, creating if not existing."""
    os.makedirs(CHROMA_DB_DIR, exist_ok=True)
    client = PersistentClient(path=CHROMA_DB_DIR)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def store_embeddings(chunks, embeddings, metadatas, ids):
    """Stores embeddings and related data in ChromaDB."""
    collection = init_chroma()

    collection.upsert(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

    return f"✅ Stored {len(ids)} embeddings in ChromaDB"

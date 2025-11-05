import os
from typing import List, Tuple
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient

from lexetl.config import EMBEDDING_MODEL_NAME, CHROMA_DB_DIR, COLLECTION_NAME


def get_embedder():
    return SentenceTransformer(EMBEDDING_MODEL_NAME)


def get_chroma_collection():
    client = PersistentClient(path=CHROMA_DB_DIR)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def embed_chunks(chunks: List[str]) -> Tuple[list, list, list]:
    """
    Embeds text chunks and returns (embeddings, metadatas, ids)
    """
    model = get_embedder()
    embeddings = model.encode(chunks, convert_to_numpy=True, show_progress_bar=False)

    metadatas = [{"length": len(c)} for c in chunks]
    ids = [f"doc_{i}" for i in range(len(chunks))]

    return embeddings.tolist(), metadatas, ids

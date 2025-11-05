from typing import List, Tuple
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
from lexetl.config import EMBEDDING_MODEL_NAME, CHROMA_DB_DIR, COLLECTION_NAME


def get_embedder():
    return SentenceTransformer(EMBEDDING_MODEL_NAME)


def get_chroma_collection():
    client = PersistentClient(path=CHROMA_DB_DIR)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def embed_chunks(chunks: List[dict]) -> Tuple[list, list, list, list]:
    """
    Takes list of dicts: [{file, chunk_id, text}, ...]
    Returns tuple: (texts, embeddings, metadatas, ids)
    """
    if not chunks:
        return [], [], [], []

    texts = [c["text"] for c in chunks]
    metadatas = [{"file": c["file"], "chunk_id": c["chunk_id"]} for c in chunks]
    ids = [f"{c['file']}_{c['chunk_id']}" for c in chunks]

    model = get_embedder()
    embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=False)

    return texts, embeddings.tolist(), metadatas, ids

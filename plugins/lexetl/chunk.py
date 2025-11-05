from nltk.tokenize import sent_tokenize
from lexetl.clean import clean_text


def chunk_text_hybrid(text, max_tokens=200):
    """
    Splits text into chunks using sentences first, then falls back to token slicing.
    """
    sentences = sent_tokenize(text)
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len((current_chunk + sentence).split()) <= max_tokens:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def chunk_data(docs, max_tokens=200):
    """
    Accepts list of tuples: [(filename, cleaned_text), ...]
    Returns list of dict chunks: [{file, chunk_id, text}]
    """
    results = []
    for file, text in docs:
        cleaned = clean_text(text)
        chunks = chunk_text_hybrid(cleaned, max_tokens=max_tokens)
        for i, chunk in enumerate(chunks):
            results.append({
                "file": file,
                "chunk_id": i,
                "text": chunk
            })
    return results

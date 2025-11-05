import re

def clean_text(text: str) -> str:
    """Basic text normalization."""
    if not isinstance(text, str):
        return ""
    text = text.replace("\n", " ").strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9.,;:!?()\-\'\" ]", "", text)
    return text


def clean_data(docs):
    """
    Accepts list of tuples [(filename, text), ...]
    Returns cleaned list with same structure.
    """
    cleaned = []
    for file, text in docs:
        cleaned.append((file, clean_text(text)))
    return cleaned

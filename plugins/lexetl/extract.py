import os
import json
import csv
from lexetl.ocr_utils import pdf_to_text
from lexetl.config import RAW_DIR


def load_json_files(path=os.path.join(RAW_DIR, "jsons")):
    docs = []
    if not os.path.exists(path):
        return docs
    for file in os.listdir(path):
        if file.endswith(".json"):
            with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                data = json.load(f)
                docs.append((file, data.get("text", "")))
    return docs


def load_csv_files(path=os.path.join(RAW_DIR, "csvs")):
    docs = []
    if not os.path.exists(path):
        return docs
    for file in os.listdir(path):
        if file.endswith(".csv"):
            with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                text = " ".join([" ".join(row) for row in reader])
                docs.append((file, text))
    return docs


def load_pdf_files(path=os.path.join(RAW_DIR, "pdfs")):
    docs = []
    if not os.path.exists(path):
        return docs
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            full_path = os.path.join(path, file)
            text = pdf_to_text(full_path)
            docs.append((file, text))
    return docs


# ✅ Wrapper used by Airflow DAG
def extract_data():
    """
    Returns a list of tuples (filename, text)
    combining JSON, CSV and PDF extracted text.
    """
    docs = []
    docs.extend(load_json_files())
    docs.extend(load_csv_files())
    docs.extend(load_pdf_files())
    return docs


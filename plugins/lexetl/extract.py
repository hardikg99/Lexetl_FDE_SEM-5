import os
import json
import csv
from lexetl.ocr_utils import pdf_to_text
from lexetl.config import RAW_DIR


def load_json_files(path=os.path.join(RAW_DIR, 'jsons')):
    docs = []
    for file in os.listdir(path):
        if file.endswith('.json') or file.endswith('.jsonl'):
            full_path = os.path.join(path, file)
            with open(full_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                if isinstance(data, list):
                    for idx, item in enumerate(data):
                        text = item.get('text') or item.get('question') or json.dumps(item)
                        docs.append((f'{file}_{idx}', text))

                elif isinstance(data, dict):
                    text = data.get('text', json.dumps(data))
                    docs.append((file, text))
    return docs


def load_csv_files(path=os.path.join(RAW_DIR, 'csvs')):
    docs = []
    for file in os.listdir(path):
        if file.endswith('.csv'):
            full_path = os.path.join(path, file)
            with open(full_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                text = ' '.join([' '.join(row) for row in reader])
                docs.append((file, text))
    return docs


def load_pdf_files(path=os.path.join(RAW_DIR, 'pdfs')):
    docs = []
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            full_path = os.path.join(path, file)
            text = pdf_to_text(full_path)
            docs.append((file, text))
    return docs


def extract_data():
    docs = []
    docs.extend(load_json_files())
    docs.extend(load_csv_files())
    docs.extend(load_pdf_files())
    return docs

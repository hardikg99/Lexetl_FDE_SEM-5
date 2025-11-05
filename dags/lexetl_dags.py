from datetime import datetime
from airflow.decorators import dag, task

# Import your pipeline functions
from lexetl.extract import extract_data
from lexetl.clean import clean_data
from lexetl.chunk import chunk_data
from lexetl.embed import embed_chunks
from lexetl.store import store_embeddings
from lexetl.evaluate import evaluate_embeddings


@dag(
    dag_id='lexetl_pipeline',
    description='End-to-end ETL pipeline for legal document embeddings',
    start_date=datetime(2024, 1, 1),
    schedule=None,           # Manual trigger only
    catchup=False,
    tags=['lexetl', 'pipeline', 'embeddings']
)
def lexetl_dag():

    @task
    def extract_task():
        return extract_data()

    @task
    def clean_task(raw_docs):
        return clean_data(raw_docs)

    @task
    def chunk_task(cleaned_docs):
        # Modify this line to reduce the size of data for testing
        return chunk_data(cleaned_docs)[:100]  # Only first 100 chunks to test

    @task
    def embed_task(chunks):
        return embed_chunks(chunks)

    @task
    def store_task(data):
        texts, embeddings, metadatas, ids = data
        return store_embeddings(texts, embeddings, metadatas, ids)

    @task
    def evaluate_task(msg):
        return evaluate_embeddings(msg)

    # Pipeline flow
    raw = extract_task()
    cleaned = clean_task(raw)
    chunks = chunk_task(cleaned)
    embedded = embed_task(chunks)
    stored = store_task(embedded)
    evaluate_task(stored)


# This will trigger the DAG execution when you run it manually
lexetl_dag()

Start all containers:
docker-compose up -d

Open Airflow UI:
http://localhost:8080

Username: airflow
Password: airflow

Place your raw data inside:
data/raw/jsons/
data/raw/csvs/
data/raw/pdfs/

Trigger DAG lexetl_pipeline from the Airflow UI.

Stop all containers:
docker compose down
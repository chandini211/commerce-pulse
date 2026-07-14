from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    "owner": "Krishna Patel",
    "retries": 1,
}

with DAG(
    dag_id="olist_etl_pipeline",
    description="ETL Pipeline for Olist Dataset",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=["ETL", "PostgreSQL"],
) as dag:

    extract = BashOperator(
        task_id="extract_data",
        bash_command="cd /opt/airflow/project && python etl/extract.py",
    )

    transform = BashOperator(
        task_id="transform_data",
        bash_command="cd /opt/airflow/project && python etl/transform.py",
    )

    load = BashOperator(
        task_id="load_data",
        bash_command="cd /opt/airflow/project && python etl/load.py",
    )

    extract >> transform >> load
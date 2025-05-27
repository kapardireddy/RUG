from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from meteo_etl import run_meteo


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 3),
    'email': ['kapardi21@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='meteo_dag',
    default_args=default_args,
    description='dag to push data to s3 bucket',
    schedule=timedelta(days=1),  # ✅ updated for Airflow 3
)

run_etl = PythonOperator(
    task_id='meteo_run',
    python_callable = run_meteo,
    dag=dag, 
)

run_etl
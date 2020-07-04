from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

with DAG('my_dag', start_date=datetime(2020, 1, 1))  as dag:
    op = DummyOperator(task_id='op')
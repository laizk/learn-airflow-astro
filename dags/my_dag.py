from airflow.sdk import dag, task, DAG
from pendulum import datetime

with DAG(
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    description="This dags does...",
    tags=["team_a", "source_a"],
    max_consecutive_failed_dag_runs=3
):

    @task
    def task_a():
        print("Hello from task A!")
        
    task_a()



from airflow.sdk import dag
from pendulum import datetime

@dag(
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    description="This dags does...",
    tags=["team_a", "source_a"],
    max_consecutive_failed_dag_runs=3
)
def my_dag():
    pass

my_dag()
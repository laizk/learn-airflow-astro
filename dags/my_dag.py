from airflow.sdk import dag, task
from pendulum import datetime

default_args ={
    'retries': 3
}

@dag(
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    description="This dags does...",
    tags=["team_a", "source_a"],
    max_consecutive_failed_dag_runs=3,
    default_args=default_args,
)
def my_dag():
    
    @task
    def task_a():
        print("Hello, Airflow!")
        
    task_a()
    
my_dag()
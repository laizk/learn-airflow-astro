from airflow.sdk import dag, task, chain
from pendulum import datetime

default_args ={
    'retries': 3
}  

@dag(
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    description="DAG to check data",
    tags=["data_engineering"],
    max_consecutive_failed_dag_runs=3,
    default_args=default_args,
)
def check_dag():
    
    @task.bash
    def create_file():
        return 'echo "Hi there!" > /tmp/dummy'
        
    @task.bash
    def check_file():
        return 'test -f /tmp/dummy'
        
    @task
    def read_file():
        print(open('/tmp/dummy', 'rb').read())
    
    chain(create_file(), check_file(), read_file())
    
check_dag()
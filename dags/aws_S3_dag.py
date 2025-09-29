from airflow.decorators import dag, task
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['aws']
)
def aws_s3_dag():
    wait_for_file = S3KeySensor(
        task_id='wait_for_file',
        aws_conn_id='aws_default',
        bucket_key="s3://learn-airflow-t0pz/data_*",
        wildcard_match=True
    )
    
    @task
    def process_file():
        print("There is a processing of file!")
    
    
    wait_for_file >> process_file() 
    
aws_s3_dag()
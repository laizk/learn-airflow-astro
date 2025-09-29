from airflow.sdk import dag, task, Context

@dag
def xcom_dag():
    
    @task
    def task_a(ti):
        val = 42
        ti.xcom_push(key="my_key", value=val)
        
        
    @task
    def task_b(ti):
        ti.xcom_pull(task_ids="task_a", key="my_key")
    
    task_a() >> task_b()
    
    
xcom_dag()
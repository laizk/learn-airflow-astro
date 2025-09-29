from airflow.sdk import dag, task, Context

@dag
def xcom_dag():
    
    @task
    def task_a(**context: Context):
        val = 42
        return val # equivalent to context['ti'].xcom_push(key='my_key', value = val)
        
        
    @task
    def task_b(value: int):
        print(value)
    
    val = task_a()
    task_b(val)
    
    
xcom_dag()
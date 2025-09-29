from airflow.sdk import dag, task, Context

@dag
def xcom_dag():
    
    @task
    def task_a(ti):
        val = {
            "val_1": 42,
            "val_2" : 43
        }
        ti.xcom_push(key="my_key", value=val)
        
     
    @task
    def task_c(ti):
        val = 43
        ti.xcom_push(key="my_key", value=val)   
        
    @task
    def task_b(ti):
        vals = ti.xcom_pull(task_ids=["task_a", "task_c"], key="my_key")
        print(vals)
    
    task_a() >> task_c() >>task_b()
    
    
xcom_dag()
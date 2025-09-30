from airflow.sdk import dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

@dag
def snowflake():
    task='run_a_query'
    sql="SELECT * FROM my_table",
    conn_id=""
    
snowflake()
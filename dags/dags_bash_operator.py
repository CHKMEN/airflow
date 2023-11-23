from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime
import pendulum

with DAG(
    dag_id="dags_bash_operator", # airflow에 표시되는이름, 파일명과 맞추는게 좋다.
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"), # UTC 세계표준시는 한국시간보다 9시간 느리다.
    catchup=False # 누락된 구간을 돌리지 않는다. 일반적으로는 False로 사용한다.
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1", # 객체명과 task id는 동일하게 맞추는게 좋다.
        bash_command="echo whoami",
    )
        
    bash_t2 = BashOperator(
        task_id="bash_t2", # 객체명과 task id는 동일하게 맞추는게 좋다.
        bash_command="echo $HOSTNAME",
    )
        
    bash_t1 >> bash_t2
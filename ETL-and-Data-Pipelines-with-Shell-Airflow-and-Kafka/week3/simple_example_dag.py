#import libraries
from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime as dt

#import dag arguments 
default_args= {
    "owner": "felix",
    "email": ["felixpratama242@gmail.com"], 
    "start_date": dt.datetime(2023, 4, 21),
    "retries": 1, # the number times it should keep trying if it is failling: here only one if it does fail
    "retry_delay": dt.timedelta(minutes=5) # time to wait between subsequent tries
}

#DAG Definition
dag = DAG('simple_example',
          description="A simple example DAG",
          default_args=default_args,
          schedule=dt.timedelta(seconds=5)# Scheduling instructions. In this case, the DAG will run repeatedly on a schedule interval of five seconds once it is deployed 
          )

#task definition
task1 = BashOperator(
    task_id = "print_hello",
    bash_command = "echo 'Greetings. The date and time are'",
    dag = dag
)

task2 = BashOperator(
    task_id = "print_date",
    bash_command = 'date',
    dag = dag
)

#task pipeline
task1 >> task2 
#double greater than notation specifies that task two is downstream from task one
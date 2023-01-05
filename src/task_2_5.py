
# Import the required libraries
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

# Set default_args dictionary to specify default parameters of the DAG, such as the start date and frequency of runs
default_args = {
    'owner': 'me',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Create a DAG instance and pass it the default_args dictionary
dag = DAG(
    'task_2_5',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

# Create DummyOperator instances for each task
task1 = DummyOperator(task_id='task_1', dag=dag)
task2 = DummyOperator(task_id='task_2', dag=dag)
task3 = DummyOperator(task_id='task_3', dag=dag)
task4 = DummyOperator(task_id='task_4', dag=dag)
task5 = DummyOperator(task_id='task_5', dag=dag)
task6 = DummyOperator(task_id='task_6', dag=dag)

# Set task dependencies
task1 >> [task2, task3] >> [task4, task5, task6]

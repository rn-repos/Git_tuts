from airflow import DAG
from airflow import timedelta,datetime
from airflow.operators import pythonOPerator
from airflow.operators import Bashopeatros
from airflow.operators import create BigqueryCreateEmptyTable operators

#run a DAG Every Friday at 4 PM

default_args={
'owner':airflow1,
start_date:(2024,03,14),
email_on_failure:'false',
retries:1
retry_delay=timedelta(minutes=5)

}

dag=DAG(

default_args=default_args,
schedule_interval=(0,16,0,0),
email_on_failure='false',
retry_on_failure='false',
)

project_id='your_project',
dataset_id='your_dataset',
table_id='your_table'
table_schema=[{
id='col1',type='integer'},
name='col2',type='string']
create_table_task=Create BigqueryEmptyTableOperator(
)
from airflow import DAG
from airflow.operators import pythonOpertor
from airflow.operators import dummyOperator
from datetime import timedelta,datetime
from airflow import BashOperator

default_args={
'owner':name
start_date:(2024,11,02)
retries:1
retry_delay=timedelta(minutes=5)



}
dag=DAG(
default_args=default_args
email_on_failure='False'
retry_on_failure='False'
schedule_interval=('0 16 0 0')

)


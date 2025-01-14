from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import json
import requests

default_args = {
    'owner':'Rohith',
    'Start_date': datetime(2025,1,9,2,00)
    
}

def get_data():
    res=requests.get("https://randomuser.me/api/")
    res=res.json()
    res=res['results'][0]
    
    return res

def format_data(res):
    data={}
    

def stream_data

# with DAG('user_automation',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:
    
#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable=stream_data
#     )
    

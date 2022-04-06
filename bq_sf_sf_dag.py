from src.controller.mainDAG import DAGBuilder, DAGControl
from airflow.operators.python_operator import PythonOperator

def run_DAG(**context):
    dag_flow = DAGControl()
    dag_flow._start_loading()

builder = DAGBuilder()
dag = builder.create_dag()

with dag:
    task = PythonOperator(
        task_id='SFLK_BQ_LOADER',
        python_callable=run_DAG,
        provide_context=False,
        dag=dag
    )    
from datetime import datetime
import pendulum
from airflow import DAG

class DAGSConfig:
    def __init__(self,dag_name,schedule_interval,dag_owner,dag_start_date,operator_email,email_on_failure,email_on_retry,timezone):
        self._dag_name = dag_name
        self._schedule = schedule_interval
        self._dag_owner = dag_owner
        self._dag_start_date = dag_start_date
        self._operator_email = operator_email
        self._email_on_failure =email_on_failure
        self._email_on_retry = email_on_retry
        self._timezone = timezone
        self._local_tz = pendulum.timezone(self._timezone)

    
    def _get_DAGArgs(self):
        return {'owner':self._dag_owner,
                'start_date':datetime(self._dag_start_date,tzinfo = self._local_tz),
                'email':self._operator_email,
                'email_on_retry':self._email_on_retry,
                'email_on_failure':self._email_on_failure}

    def _get_DAGObj(self):
        self._args = self._get_DAGArgs()
        return DAG(dag_id=self._dag_name,
                   default_args=self._args,
                   schedule_interval=self._schedule,
                   catchup=False,
                   max_active_runs=1)
                   

from airflow import DAG
from airflow.operators.python_operator import PytonOpertor

from goolge.cloud import bigquery

from snowflake.connector.pandas_tools import write_pandas

from simple_salesforce import SalesForce

from datetime import datetime
import pendulum
import logging
import pandas
import pandas_gbq


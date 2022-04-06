from src.controller.BQLoadJob import BQLoader
from src.controller.SFLKLoadJob import SFLKLoader
from src.config.Salesforce_Config import SalesForceConfig
import pandas as pd

class DAGControl:
    def __init__(self):
        self._sflkLoader = SFLKLoader()
        self._bqLoader = BQLoader() 
        self._sfConfig = SalesForceConfig(object_name='',username='',password='',token='')
    
    def _start_loading(self):
        sf_con = self._sfConfig._get_con()
        fields = self._sfConfig._get_fieldNames()
        soql = self._sfConfig._get_soql()
        sf_data = sf_con.query_all(soql)
        df = pd.DataFrame(sf_data['records']).drop(columns='attributes')

        print('STARTING BIGQUERY LOADING')
        self._bqLoader._start_loading(df)

        print('STARTING SNOWFLAKE LOADING')
        self._sflkLoader._start_loading(df)
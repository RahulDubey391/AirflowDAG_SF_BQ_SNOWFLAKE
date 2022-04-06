from src.config.BQConfig import BQConfig
import pandas_gbq

class BQLoader:
    def __init__(self):
        self._bqConfig = BQConfig(project_id='',dataset_name='',table_name='')
        self.bq_con = self._bqConfig._get_con()
    
    def _start_loading(self,df):
        table_ref = self._bqConfig._dataset_name + '.' + self._bqConfig._table_name
        pandas_gbq.to_gbq(df,table_ref,self._bqConfig._project_id,if_exists='append')
        print('LOADING BQ DONE')        

from src.config.Snowflake_Config import SnowflakeConfig
from snowflake.connector.pandas_tools import write_pandas

class SFLKLoader:
    def __init__(self):
        self._sflk = SnowflakeConfig(con_id='',database='',schema_name='',table_name='')
        self._sflk_con = self._sflk._get_con()
        self._sflk_cur = self._sflk._get_cur()
    
    def _start_loading(self,df):
        write_pandas(self._sflk_con,df,self._sflk._table_name,self._sflk._schema_name)
        print('SNOWFLAKE LOADING DONE')
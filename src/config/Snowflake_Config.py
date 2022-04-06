from airflow.contrib.hooks.snowflake_hook import SnowflakeHook

class SnowflakeConfig:
    def __init__(self,con_id,database,schema_name,table_name):
        self._con_id = con_id
        self._database = database
        self._schema_name = schema_name
        self._table_name = table_name 
    
    def _get_con(self):
        return SnowflakeHook(snowflake_conn_id=self._con_id,
                             database=self._database)
    
    def _get_cur(self):
        return self._get_con().cursor()

    def _set_columns(self,columns):
        self._tgt_sf_columns = columns



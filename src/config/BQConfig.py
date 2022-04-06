from google.cloud import bigquery

class BQConfig:
    def __init__(self,project_id,dataset_name,table_name):
        self._project_id = project_id
        self._dataset_name = dataset_name
        self._table_name = table_name
    
    def _get_con(self):
        client = bigquery.Client(self._project_id)
        return client
    
            

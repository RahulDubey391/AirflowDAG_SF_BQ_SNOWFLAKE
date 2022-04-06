from simple_salesforce import Salesforce

class SalesForceConfig:
    def __init__(self,object_name,username,password,token):
        self._object_name = object_name
        self._username = username
        self._password = password
        self._token = token

    def _get_con(self):
        sf = Salesforce(username=self._username,
                          password=self._password,
                          security_token=self._token)
        return sf

    def _get_fieldNames(self):
        sf = self._get_con()
        desc = getattr(sf,self._object_name).describe()
        fieldNames = [field['name'] for field in desc['fields']]
        return fieldNames
    
    def _get_soql(self,field_names):
        soql = "SELECT {} FROM {}".format(i = ','.join(field_names),j=self._object_name)
        return soql
    


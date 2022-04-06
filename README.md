# AirflowDAG_SF_BQ_SNOWFLAKE
 This is a template DAG which can be used to access and load the data from SalesForce Object to BigQuery and Snowflake simulatenously

A few things to keep in mind:
 1. You have setup a Snowflake Connection in "Connections" of the Aiflow Environment. This will ensure the security of your credentials.
 2. Keep the "SRC" directory in the bucket only and not in any other subfolder.
 3. Also the main dag file "bq_sf_sf_dag.py" will be at the root of bucket. The Airflow looks for the DAG definition in every file to upload the Configurations/Trees to UI Server.
 4. Be sure to set empty credentials/configurations according to your needs.

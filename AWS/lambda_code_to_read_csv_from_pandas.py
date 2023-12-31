import json
import boto3
import pandas as pd

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print(event)                                           # Actual records in json format
    print(context)                                         # Metadata 
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        s3_file_name = event['Records'][0]['s3']['object']['key']
        resp = s3_client.get_object(Bucket = bucket_name ,Key = s3_file_name )
        print(resp['Body'])
        df_s3_data = pd.read_csv(resp['Body'], sep = ',')
        print(df_s3_data.head())
    except Exception as err:
        print(err)

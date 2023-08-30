import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket = s3.Bucket('bucket1-basic1')
    print('Here ',bucket.objects.all())
    for obj in bucket.objects.all():
        key = obj.key
        print(key)

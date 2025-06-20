import json
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    delete_bucket = client.delete_bucket(
        Bucket='udemys306202025'
    )
        
    print(delete_bucket)   


import json
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    create_s3bucket=client.create_bucket(
        Bucket='udemys306202025',
        CreateBucketConfiguration={
            'LocationConstraint':'us-east-2'}
         )
         
    print(create_s3bucket)

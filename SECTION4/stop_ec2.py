import json
import boto3
client = boto3.client('ec2')

def lambda_handler(event, context):
    response = client.stop_instances(
    InstanceIds=[
        'i-0782c1932efa0c1e1'
    ]

)


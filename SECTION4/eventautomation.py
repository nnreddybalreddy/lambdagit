import json
import boto3
client=boto3.client('ec2')

def lambda_handler(event, context):
     response = client.run_instances(
     ImageId= 'ami-09c813fb71547fc4f',
     InstanceType = 't2.micro',
     MaxCount=1,
     MinCount=1)
     print(response['Instances'][0]['InstanceId'])

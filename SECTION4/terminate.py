import boto3 
client = boto3.client('ec2')
def lambda_handler(event, context):    
    response=client.terminate_instances(
        InstanceIds=[
            'i-0782c1932efa0c1e1',
            'i-082a1845c610f346a'
        ]
    )

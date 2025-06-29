import json

#1 Import boto3 and create client connection with bedrock
import boto3
client = boto3.client('bedrock-runtime')
#print(boto3.__version__)

def lambda_handler(event, context):
    
# 4 a. Print the event , b. Store the input in a variable, c. Update the response body
    print(event)
    user_prompt=event['prompt']

#2 Create a Request Syntax - Get details from console and body should be json object

    response = client.invoke_model(
        accept='application/json',
        body=json.dumps({"prompt": user_prompt,"temperature": 0.9,"max_tokens": 100}),
        contentType='application/json',
        modelId='cohere.command-text-v14')
    print(response['body'])
    
#3 Convert Streaming Body to Byte and then Byte to String
    response_byte=response['body'].read()
    response_string=json.loads(response_byte)

    return {
        'statusCode': 200,
        'body': response_string
    }

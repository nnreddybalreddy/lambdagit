def lambda_handler(event, context):
    
#1.Log the event
   print("The event data is below")
   print(event)
   
   authorization = 'Deny'
   
#2. Validate the token
   if event['authorizationToken']=='123456':
       authorization = 'Allow'
       
   else:
       authorization='Deny'
       
#3 . Generate the IAM Policy

   authorizationpolicy = {"principalId": "rahulpolicy","policyDocument": {"Version": "2012-10-17","Statement": [{"Action": "execute-api:Invoke","Effect": authorization,"Resource": ["arn:aws:execute-api:us-east-1:196715057542:7lq3y19ycl/dev/GET/students"]}]}}
   return authorizationpolicy

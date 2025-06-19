response={
    'Buckets': [
        {
            'Name': 'string',
            'CreationDate': 25
        },
    ],
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    },  
}

print(response['Buckets']) # [{'Name': 'string', 'CreationDate': 25}]
print(response['Buckets'][0]) # {'Name': 'string', 'CreationDate': 25}
print(response['Buckets'][0]['Name']) # string

print(response['Owner']) # {'DisplayName': 'string', 'ID': 'string'}
print(response['Owner']['DisplayName']) # string


# List 

list=[1,4,"For","Anisha"]

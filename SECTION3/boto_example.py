# # response={
# #     'Buckets': [
# #         {
# #             'Name': 'string',
# #             'CreationDate': 25
# #         },
# #     ],
# #     'Owner': {
# #         'DisplayName': 'string',
# #         'ID': 'string'
# #     },  
# # }

# # print(response['Buckets']) # [{'Name': 'string', 'CreationDate': 25}]
# # print(response['Buckets'][0]) # {'Name': 'string', 'CreationDate': 25}
# # print(response['Buckets'][0]['Name']) # string

# # print(response['Owner']) # {'DisplayName': 'string', 'ID': 'string'}
# # print(response['Owner']['DisplayName']) # string


# # # List 

# list1=[1,4,"For","Anisha"]
# # print(list[1]) #4

# print(list1[0:2:1]) # [1, 4]

# # Nested List 
# NestedList=[[1,2,3],[4,5,6],[7,8,9]]

# print(NestedList[0]) # [1, 2, 3]
# print(NestedList[0][1]) # 2
# print(NestedList[2][2]) #9

response={
    'Buckets': [
        {
            'Name': 'bucket1',
            'CreationDate': 25
        },
        {
            'Name': 'bucket2',
            'CreationDate': 30
        }
    ],
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    },  
}

print(response['Buckets']) # [{'Name': 'bucket1', 'CreationDate': 25}, {'Name': 'bucket2', 'CreationDate': 30}]
print(response['Buckets'][0]) # {'Name': 'bucket1', 'CreationDate':
print(response['Buckets'][1]['Name']) # bucket2

# Function

def evenOdd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


evenOdd(2) # Even
evenOdd(3) # Odd
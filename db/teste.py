import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('MinhaTabela')

table.put_item(
    Item={
        'ID': '456',
        'Nome': 'Maria'
    }
)
print("Item inserido com sucesso!")

response = table.get_item(Key={'ID': '456'})
if 'Item' in response:
    print("Item encontrado:", response['Item'])
else:
    print("Item não encontrado.")
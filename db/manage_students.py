import boto3
from decimal import Decimal

# Conectar ao DynamoDB local
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Tabelas
students_table = dynamodb.Table('Students')
courses_table = dynamodb.Table('CourseRegistrations')

# Novos itens para a tabela Students
students_items = [
    {'StudentId': 'S005', 'Name': 'Eduardo Lima', 'Grade': Decimal('7.5')},
    {'StudentId': 'S006', 'Name': 'Fernanda Souza', 'Grade': Decimal('8.0')},
    {'StudentId': 'S007', 'Name': 'Gabriel Almeida', 'Grade': Decimal('6.8')}
]

# Novos itens para a tabela CourseRegistrations
courses_items = [
    {'StudentId': 'S005', 'CourseCode': 'HIST101', 'RegistrationDate': '2023-03-01', 'Status': 'Active'},
    {'StudentId': 'S005', 'CourseCode': 'CS101', 'RegistrationDate': '2023-03-05', 'Status': 'Active'},
    {'StudentId': 'S006', 'CourseCode': 'ENG201', 'RegistrationDate': '2023-04-01', 'Status': 'Pending'}
]

# Adicionar itens à tabela Students
print("Adicionando novos alunos à tabela Students...")
for item in students_items:
    students_table.put_item(Item=item)
    print(f"Inserido: {item}")

# Adicionar itens à tabela CourseRegistrations
print("\nAdicionando novas matrículas à tabela CourseRegistrations...")
for item in courses_items:
    courses_table.put_item(Item=item)
    print(f"Inserido: {item}")

# Exemplo de consulta: Buscar um aluno
print("\nConsultando aluno S005...")
response = students_table.get_item(Key={'StudentId': 'S005'})
if 'Item' in response:
    print("Aluno encontrado:", response['Item'])
else:
    print("Aluno não encontrado.")

# Exemplo de consulta: Buscar todas as matrículas de um aluno
print("\nConsultando matrículas do aluno S005...")
response = courses_table.query(
    KeyConditionExpression='StudentId = :sid',
    ExpressionAttributeValues={':sid': 'S005'}
)
for item in response.get('Items', []):
    print("Matrícula encontrada:", item)
import boto3

mensagens = []
numMsgsToCreate = 3000
for num in range(numMsgsToCreate):
    mensagens.append({'Id':str(num), 'MessageBody': str(num)})

splitMsg = [mensagens[x:x+10] for x in range(0, len(mensagens), 10)]

sqs = boto3.client('sqs', region_name ='us-east-1')

queue_url='< URL DA FILA>' 

for lista in splitMsg:    
    print(type(lista))
    print(str(lista))
    response = sqs.send_message_batch(
        QueueUrl=queue_url,
        Entries=lista
    )
    print(response)

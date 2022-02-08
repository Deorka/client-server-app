import socket, uuid, random, string


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сокета
IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
id_client = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org'))
client.connect((IP, PORT))  # устанавливаем данные для прослушивания данного порта
client.send(id_client.encode('utf8'))
key = client.recv(1024)  # получаем ключ
print('key = ', key.decode('utf8'))

PORT1 = 8001
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((IP, PORT1))
symbols = string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
message = ''.join(random.sample(symbols, random.randint(10, 30)))  # генерируем рандомное текстовое сообщение
print('message = ', message)
client1.send(message.encode('utf8'))
client1.send(id_client.encode('utf8'))
client1.send(key)
result = client1.recv(1024)
print(result.decode('utf8'))

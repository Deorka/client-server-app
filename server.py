import socket, random, string, logging


IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
PORT1 = 8001
client = {}  # Массив для хранения адресов клиентов
logging.basicConfig(filename="sample.log", level=logging.INFO)

while True:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сокета
    server.bind((IP, PORT))  # устанавливаем данные для прослушивания данного порта
    server.listen(50)  # разрешаем серверу принимать запросы
    user, address = server.accept()  # в случае найденного пользователя разрешаем ему подключиться
    symbols = string.digits + string.ascii_uppercase + string.ascii_lowercase
    data = user.recv(1024).decode('utf8')  # получить 1024 байт данных
    if data not in client.keys():
        key = ''.join(random.sample(symbols, 8))  # сгенерировать код новому клиенту
        client.update({data: key})  # Если такого клиента нету , то добавить его и сгенерированный код
        print(data, '    => ', key)
        user.send(key.encode('utf8'))

    server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server1.bind((IP, PORT1))
    server1.listen(50)  # разрешаем серверу принимать запросы
    user1, address1 = server1.accept()
    message = user1.recv(1024).decode('utf8')  # получить 1024 байт данных
    id_client = user1.recv(1024).decode('utf8')
    key_client = user1.recv(1024).decode('utf8')
    if id_client in client.keys():
        if client[data] == key_client:
            logging.info(message)
            user1.send('ok'.encode('utf8'))
        else:
            logging.error("Wrong key")
            user1.send('Wrong key'.encode('utf8'))
    else:
        logging.error("Get the key first")
        user1.send('Get the key first'.encode('utf8'))

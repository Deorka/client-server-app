import socket, uuid, random, string

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
PORT1 = 8001


def send_id_and_rec_key():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сокета
    client.connect((IP, PORT))  # устанавливаем данные для прослушивания данного порта
    client.send(id_client.encode('utf8'))
    key = client.recv(1024)  # получаем ключ
    return key


def send_message(key):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT1))
    symbols = string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
    message = ''.join(random.sample(symbols, random.randint(10, 30)))  # генерируем рандомное текстовое сообщение
    print('message = ', message)
    client.send(message.encode('utf8'))
    client.send(id_client.encode('utf8'))
    client.send(key)


if __name__ == '__main__':
    id_client = str(uuid.uuid4())
    k = send_id_and_rec_key()
    send_message(k)

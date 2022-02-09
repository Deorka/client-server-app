import socket, uuid
from utils import generate_message

IP = 'localhost'
PORT = 8000
PORT1 = 8001


def send_id_and_rec_key(id_cl):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сокета
    client.connect((IP, PORT))  # устанавливаем данные для прослушивания данного порта
    client.send(id_cl.encode('utf8'))
    key = client.recv(1024)  # получаем ключ
    return key


def send_message(key, id_cl):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT1))
    message = generate_message()  # генерируем рандомное текстовое сообщение
    client.sendall(f'{message} {id_cl} {key.decode("utf8")}'.encode('utf8'))
    answer = client.recv(1024)
    print(answer.decode('utf8'))


if __name__ == '__main__':
    id_client = str(uuid.uuid4())
    k = send_id_and_rec_key(id_client)
    send_message(k, id_client)

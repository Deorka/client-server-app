import socket, random, string, logging


IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
PORT1 = 8001
CLIENT = {}  # Массив для хранения адресов клиентов


def generate_and_send_key_for_new_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:  # создание сокета
        server.bind((IP, PORT))  # устанавливаем данные для прослушивания данного порта
        server.listen(50)  # разрешаем серверу принимать запросы
        user, address = server.accept()  # в случае найденного пользователя разрешаем ему подключиться
        symbols = string.digits + string.ascii_uppercase + string.ascii_lowercase
        data = user.recv(1024).decode('utf8')  # получить 1024 байт данных
        if data not in CLIENT.keys():
            key = ''.join(random.sample(symbols, 8))  # сгенерировать код новому клиенту
            CLIENT.update({data: key})  # Если такого клиента нету , то добавить его и сгенерированный код
            user.send(key.encode('utf8'))


def check_client_and_write_message_in_log():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((IP, PORT1))
        server.listen(50)  # разрешаем серверу принимать запросы
        user, address = server.accept()
        message = user.recv(1024).decode('utf8')  # получить 1024 байт данных
        id_client = user.recv(1024).decode('utf8')
        key_client = user.recv(1024).decode('utf8')
        if id_client in CLIENT.keys():
            if CLIENT[id_client] == key_client:
                logging.info(message)
            else:
                logging.error("Wrong key")
        else:
            logging.error("Get the key first")


if __name__ == '__main__':
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    generate_and_send_key_for_new_client()
    check_client_and_write_message_in_log()


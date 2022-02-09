import socketserver, string, logging, os

HOST, PORT = "localhost", 8001


class MyTCPHandler(socketserver.BaseRequestHandler):
    symbols = string.digits + string.ascii_uppercase + string.ascii_lowercase

    def handle(self):
        client = {}
        if os.stat("clients.txt").st_size > 5:
            with open('clients.txt') as c:
                for line in c:
                    client.update({line.split(' ')[0]: line.split(' ')[1]})

        clients = open('clients.txt', 'a')
        message, id_client, key_client = self.request.recv(1024).strip().decode('utf8').split(
            ' ')  # получить 1024 байт данных

        print(key_client, '\n')

        if id_client in client.keys():
            if client[id_client].strip() == key_client:
                logging.info(message)
            else:
                logging.error("Wrong key")
        else:
            logging.error("Get the key first")


if __name__ == "__main__":
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

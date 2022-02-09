import socketserver, logging
from utils import file_data_to_dictionary

HOST, PORT = "localhost", 8001


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        client = file_data_to_dictionary()

        r = self.request.recv(1024)
        message, id_client, key_client = r.strip().decode('utf8').split(' ')  # получить данные

        if id_client in client.keys():
            if client[id_client].strip() == key_client:
                logging.info(message)
            else:
                self.request.send("Wrong key".encode('utf8'))
        else:
            self.request.send("Get the key first".encode('utf8'))


if __name__ == "__main__":
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

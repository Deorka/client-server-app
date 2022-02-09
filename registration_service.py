import socketserver
from utils import file_data_to_dictionary, generate_key, NAME_DB

HOST, PORT = "localhost", 8000


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        client_id = self.request.recv(1024).strip()
        client = file_data_to_dictionary()

        with open(NAME_DB, 'a') as clients:
            if client_id not in client.keys():
                key = generate_key(10)  # сгенерировать код новому клиенту
                d = client_id.decode('utf8')
                clients.write(f'{d} {key}\n')
                self.request.sendall(key.encode('utf8'))


if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

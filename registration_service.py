import socketserver, random, string

HOST, PORT = "localhost", 8000


class MyTCPHandler(socketserver.BaseRequestHandler):
    symbols = string.digits + string.ascii_uppercase + string.ascii_lowercase

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        client = {}
        with open('clients.txt') as c:
            for line in c:
                client.update({line.split(' ')[0]: line.split(' ')[1]})

        clients = open('clients.txt', 'a')
        if self.data not in client.keys():
            key = ''.join(random.sample(self.symbols, 8))  # сгенерировать код новому клиенту
            d = self.data.decode('utf8')
            clients.write(f'{d} {key}\n')
            self.request.sendall(key.encode('utf8'))


if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

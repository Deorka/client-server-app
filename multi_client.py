import uuid
from threading import Thread
from client import send_message, send_id_and_rec_key


def threaded_function():
    id_client = str(uuid.uuid4())
    k = send_id_and_rec_key(id_client)
    send_message(k, id_client)


if __name__ == '__main__':
    threads = list()
    for _ in range(50):
        x = Thread(target=threaded_function(), args=())
        threads.append(x)
        x.start()
    for thread in threads:
        thread.join()

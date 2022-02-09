import string, random

NAME_DB = 'clients.txt'


def file_data_to_dictionary():
    """ из файла извлекает строки и преобразует в словарь {id:key} """
    client = {}
    with open(NAME_DB, 'a+') as c:
        c.seek(0)
        for line in c:
            line = line.strip()
            if line:
                client.update({line.split(' ')[0]: line.split(' ')[1]})
    return client


def generate_key(count_charact):
    """ генерирует код новому клиенту """
    symbols = string.digits + string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.sample(symbols, count_charact))


def generate_message():
    """ генерируем рандомное текстовое сообщение """
    symbols = string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.sample(symbols, random.randint(10, 30)))

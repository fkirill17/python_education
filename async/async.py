import socket

# Код серверного сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET - Протокол IPv4, SOCK_STREAM - Протокол TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Применили переиспользование адреса
server_socket.bind(('localhost', 5000))  # Установка адреса
server_socket.listen()  # Запустили прослушивание

# Код клиентского сокета
while True:
    print('Before .accept()')
    client_socket, addr = server_socket.accept()  # Блокирующая операция (Ожидает входящее подключение)
    print('Connection from', addr)

    while True:
        print('Before .recv()')
        request = client_socket.recv(4096)  # Установка размера буфера

        if not request:
            break
        else:
            response = 'Hello World\n'.encode()  # Перевод строки в байтовый вид
            client_socket.send(response)




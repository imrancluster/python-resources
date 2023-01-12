#
# Client example using socket programming
#

import socket


def _client(hostname, port):
    client_socket = socket.socket()
    client_socket.connect((hostname, port))

    message = input(" -> ")  # take input

    while message.lower().strip() != 'exit':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    client_socket.close()


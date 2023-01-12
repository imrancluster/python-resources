#
# Sever example using socket programming
#

import socket


def _server(hostname, port):
    server_sockect_instance = socket.socket()
    server_sockect_instance.bind((hostname, port))

    # two client will be connected simultaneously
    server_sockect_instance.listen(2)
    conn, address = server_sockect_instance.accept()
    print('connection from: ' + str(address))
    while True:
        # receive data from socket. won't accept greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))

        data = input('>')
        conn.send(data.encode())  # send data to the client

    conn.close()



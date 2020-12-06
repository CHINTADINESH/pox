import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 8000))
sock.listen(1)

while True:
    connection, client_address = sock.accept()

    while True:
        data = connection.recv(16)
        if data: connection.send(data)
        else: break

    connection.close()
            

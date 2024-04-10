# Servidor TCP
import socket

def tcp_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    conn, addr = server_socket.accept()

    data = conn.recv(1024).decode()
    print("Recibido de: " + str(addr))
    print("Recibido datos: " + str(data))

    conn.send(data.encode())

    conn.close()

# Cliente TCP
def tcp_client():
    host = 'localhost' #
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input(" -> ")

    client_socket.send(message.encode())

    data = client_socket.recv(1024).decode()

    print('Recibido del servidor: ' + data)

    client_socket.close()

# Servidor UDP
def udp_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    data, addr = server_socket.recvfrom(1024)

    print("Recibido de: " + str(addr))
    print("Recibido datos: " + str(data))

    server_socket.sendto(data, addr)

    server_socket.close()

# Cliente UDP
def udp_client():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input(" -> ")

    client_socket.sendto(message.encode(), (host, port))

    data, addr = client_socket.recvfrom(1024)

    print('Recibido del servidor: ' + data)

    client_socket.close()
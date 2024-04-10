import socket

def udp_server():
    host = 'localhost'  # Dirección del host
    port = 12345  # Puerto para escuchar

    # Creación del socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Servidor UDP escuchando en {}:{}".format(host, port))

    while True:
        # Recepción de datos del cliente
        data, addr = server_socket.recvfrom(1024)
        print('Mensaje recibido de {}: {}'.format(addr, data.decode()))

        # Envío de respuesta al cliente
        server_socket.sendto('Mensaje recibido'.encode(), addr)

if __name__ == '__main__':
    udp_server()
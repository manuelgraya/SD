import socket

def udp_client():
    host = 'localhost'  # Dirección del servidor
    port = 12345  # Puerto del servidor

    # Creación del socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input(" -> ")  # Mensaje para enviar al servidor

    # Envío del mensaje al servidor
    client_socket.sendto(message.encode(), (host, port))

    # Recepción de la respuesta del servidor
    data, addr = client_socket.recvfrom(1024)
    print('Recibido del servidor: ' + data.decode())

    client_socket.close()  # Cierre del socket del cliente

if __name__ == '__main__':
    udp_client()
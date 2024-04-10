import socket
# Cliente TCP
def tcp_client(): # Función que define el cliente TCP
    host = 'localhost' # IP del servidor a la que se conecta el cliente
    port = 12345 # Puerto del servidor al que se conecta el cliente

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creación del socket del cliente
    client_socket.connect((host, port)) # Conexión del cliente al servidor

    message = input(" -> ") # Mensaje que se envía al servidor a través del cliente

    client_socket.send(message.encode()) # Envío del mensaje al servidor en formato binario y lo codifica a UTF-8

    data = client_socket.recv(1024).decode() # Recepción de la respuesta del servidor 

    print('Recibido del servidor: ' + data) # Impresión de la respuesta del servidor

    client_socket.close() # Cierre del socket del cliente

if __name__ == '__main__':
    tcp_client()
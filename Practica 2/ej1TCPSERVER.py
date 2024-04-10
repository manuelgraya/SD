# Servidor TCP
import socket

def tcp_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # este es TCP socket
    server_socket.bind((host, port)) # enlaza el socket con la dirección y el puerto del servidor
    server_socket.listen(1) # escucha las conexiones entrantes 

    conn, addr = server_socket.accept() # acepta la conexión entrante del cliente

    data = conn.recv(1024).decode() # recibe los datos del cliente y los decodifica a UTF-8 
    print("Recibido de: " + str(addr)) # imprime la dirección del cliente
    print("Recibido datos: " + str(data)) # imprime los datos recibidos del cliente

    conn.send(data.encode()) # envía los datos recibidos al cliente en formato binario y los codifica a UTF-8

    conn.close() # cierra la conexión con el cliente

if __name__ == '__main__':
    tcp_server()

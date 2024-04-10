import socket

HOST = 'localhost'    # The remote host
PORT = 50007          # The same port as used by the server

# Read the binary file
with open('E:/1 CARRERA/SD/Practica 2/Examples-20240409/file2.pdf', 'rb') as f: # Abre el archivo en modo lectura binaria (read binary)
    data = f.read() # Lee el archivo y guarda los bytes en la variable data
    print(len(data)) # Muestra la cantidad de bytes del archivo

# Send the binary file to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea un socket TCP
s.connect((HOST, PORT)) # Conecta el socket al servidor
s.sendall(data) # Envía los bytes del archivo al servidor

# Send the EOT character to the server
s.send(b'\xe2\x90\x84') # Envía el caracter EOT al servidor \xe2\x90\x84 = EOF

# Receive the response from the server
data = s.recv(1024) # Recibe la respuesta del servidor
print('Received', str(data)) # Muestra la respuesta del servidor

# Close the socket
s.close()
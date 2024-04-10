import socket

HOST = 'localhost'    # The server host
PORT = 50007          # The listening port

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
s.bind((HOST, PORT)) # Bind the socket to the host and port
s.listen(1) # Escuchar una conexión

# Accept the connection from the client
conn, addr = s.accept() # Accept the connection from the client
print('Connected by', addr) # Print the address of the client
 
# Receive the data from the client
data = b''
while True:
    chunk = conn.recv(1024)
    print(len(chunk))
    print(chunk)
    find = chunk.find(b'\xe2\x90\x84')
    if find != -1:
        data += chunk[:find]
        break
    data += chunk

# write the data to a file
with open('output.pdf', 'wb') as f:
    f.write(data)

# Send the response to the client
conn.sendall(b'File received')

# Close the socket
conn.close()
s.close()


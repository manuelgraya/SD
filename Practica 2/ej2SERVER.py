#Servidor TCP
import socket
import os

def archivo_existe(nombre_archivo):
    return os.path.isfile(nombre_archivo)

def recibir_archivo(conn, nombre_archivo):
    with open(nombre_archivo, 'wb') as f:
        while True:
            datos = conn.recv(1024)
            if not datos:
                break
            f.write(datos)

def iniciar_servidor(direccion, puerto):
    servidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((direccion, puerto))
    servidor.listen(1)

    print("Servidor TCP escuchando en {}:{}".format(direccion, puerto))

    while True:
        conn, addr = servidor.accept()
        print('Conectado por', addr)

        nombre_archivo = conn.recv(1024).decode()
        print('Nombre del archivo:', nombre_archivo)

        if archivo_existe(nombre_archivo):
            conn.send(b'El archivo ya existe')
            respuesta = conn.recv(1024).decode()
            if respuesta != "SI":
                conn.close()
                continue
        else:
            conn.send(b'OK')

            recibir_archivo(conn, nombre_archivo)
            print(f"archivo {nombre_archivo} recibido")
            conn.send(b'Archivo recibido')
            conn.close()
    print ("hola")

if __name__ == '__main__':
    iniciar_servidor('localhost', 12345)

import socket
import os

def enviar_archivo(servidor, puerto, ruta_archivo):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((servidor, puerto))

    nombre_archivo = ruta_archivo.split("/")[-1] # Se obtiene el nombre del archivo
    cliente.send(nombre_archivo.encode())

    respuesta = cliente.recv(1024).decode()
    if respuesta == 'El archivo ya existe':
        print("El archivo ya existe en el servidor")
        respuesta = input("¿Desea sobreescribirlo? (SI/NO): ")
        cliente.send(respuesta.encode())
        if respuesta == "NO":
            cliente.close()
            return
        
    with open(ruta_archivo, 'rb') as f: # Abre el archivo en modo lectura binaria (read binary)
        datos = f.read()
        cliente.sendall(datos) # Envía los bytes del archivo al servidor

    print("Archivo enviado")
    notificacion = cliente.recv(1024).decode()
    if notificacion=='Archivo recibido':
        print("El archivo fue recibido por el servidor")
        os.remove(ruta_archivo)
    
    cliente.close() 

if __name__ == '__main__':
    servidor = 'localhost'
    puerto = 12345
    ruta_archivo = 'E:/1 CARRERA/SD/Practica 2/Examples-20240409/file2.pdf'
    enviar_archivo(servidor, puerto, ruta_archivo)
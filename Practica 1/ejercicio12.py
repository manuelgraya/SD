"""Implemente una función copiar(origen,destino) que copie el contenido
del fichero origen, en el fichero destino (usando open())"""

import os

os.remove("origen.txt")
#crea un archivo origen.txt con el contenido "Hola mundo"
#with open("origen.txt", "w") as file:
#    file.write("Hola mundo")

def copiar(origen, destino):
    with open(origen, 'r') as file:
        with open(destino, 'w') as file2:
            file2.write(file.read())

if __name__ == "__main__":
    origen = "origen.txt"
    destino = "destino.txt"
    copiar(origen, destino)
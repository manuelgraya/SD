""".Implemente un script en Python, utilizando el módulo os, que liste todos
los ficheros del directorio actual junto a su tamaño en bytes. Por último, el
script mostrará la suma total del tamaño de los ficheros del directorio. Se
deben incluir, además, los ficheros existentes en subdirectorios."""

import os

def listar_ficheros():
    suma = 0
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            ruta = os.path.join(root, name)
            print(ruta, os.path.getsize(ruta))
            suma += os.path.getsize(ruta)
    print("La suma total del tamaño de los ficheros del directorio es:", suma)

if __name__ == "__main__":
    listar_ficheros()
    
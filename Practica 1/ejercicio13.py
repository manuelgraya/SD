"""Imprima por pantalla el listado de directorios de inicio de los usuarios
que hay en el sistema (p. ej., /home/root , /home/osboxes, . . . ). Pista: hay
un fichero con esta información. También existe una función muy
interesante en Python llamada split, que convierte de string a lista.
"""

import os

def listado_directorios():
    with open("/etc/passwd", "r") as file:
        for line in file:
            print(line.split(":")[5])

if __name__ == "__main__":
    listado_directorios()
    
#no tengo linux gracias
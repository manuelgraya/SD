""". Realizar un script en Python que combine todos los ficheros de texto
(.txt) existentes en el directorio de trabajo actual en un único fichero de
texto, llamado “union.txt”. Tanto los ficheros con una extensión distinta,
como los que se encuentren en subdirectorios, deberán ignorarse.
"""

import os

def combinar_ficheros():
    try:
        with open("union.txt", "w") as union:
            for file in os.listdir("."):
                if file.endswith(".txt") and os.path.isfile(file):
                    with open(file, "r") as f:
                        union.write(f.read())
    except Exception as e:
        print("Ha ocurrido un error:", e)
""". Realizar un script en Python que imprima por pantalla el directorio de
trabajo actual, junto a la lista de ficheros existentes en dicho directorio.
Posteriormente, el mismo script permitirá al usuario renombrar un
fichero. Para ello solicitará al usuario el nombre del fichero que quiere
renombrar y el nuevo nombre que quiere darle. Se deben gestionar
correctamente las posibles excepciones que puedan darse en la ejecución
del script.
"""

import os

def listar_ficheros():
    print("Directorio de trabajo actual:", os.getcwd())
    print("Ficheros existentes en el directorio actual:")
    for file in os.listdir("."):
        print(file)

def renombrar_fichero():
    try:
        fichero = input("Introduzca el nombre del fichero que quiere renombrar: ")
        nuevo_nombre = input("Introduzca el nuevo nombre del fichero: ")
        os.rename(fichero, nuevo_nombre)
    except FileNotFoundError:
        print("El fichero no existe")
    except FileExistsError:
        print("El fichero ya existe")
    except PermissionError:
        print("No tiene permisos para renombrar el fichero")
    except Exception as e:
        print("Ha ocurrido un error:", e)

if __name__ == "__main__":
    listar_ficheros()
    renombrar_fichero()
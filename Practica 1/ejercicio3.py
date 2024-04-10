"""Haga un script en Python que cree una copia de un fichero cualquiera.
Puede implementar una función propia o utilizar una existente. A
continuación, utilice la librería/módulo necesario para comprobar que los
ficheros anteriores son iguales.
"""
import shutil
import filecmp
import os


ruta = 'C:/CARRERA/segundo/SD/Practica 1/ejemplos/'
archivo_origen = ruta + 'data_file.txt'
archivo_destino = './SD/Practica 1/ejemplos/copia.txt'

shutil.copy(archivo_origen, archivo_destino)

"""file1 = open(archivo_origen, 'r')
file2 = open('./SD/Practica 1/ejemplos/copia.txt', 'r')
igual = file1.read() == file2.read()
print(igual)"""

# Comparar los archivos

#comprobamos que los archivos son iguales
bool=filecmp.cmp(archivo_origen, archivo_destino, shallow=False)
print(bool)
os.remove(archivo_destino)

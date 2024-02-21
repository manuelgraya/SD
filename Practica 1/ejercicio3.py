"""Haga un script en Python que cree una copia de un fichero cualquiera.
Puede implementar una función propia o utilizar una existente. A
continuación, utilice la librería/módulo necesario para comprobar que los
ficheros anteriores son iguales.
"""
import shutil
import filecmp
import os

shutil.copy('./Practica 1/ejemplos/data_file.txt', './copia.txt')#copia el archivo data_file.txt en copia.txt

#with open('./copia.txt', 'r') as file:
#    print(file.read())

#comprobamos que los archivos son iguales
file1 = open('./Practica 1/ejemplos/data_file.txt', 'r')
file2 = open('./copia.txt', 'r')
igual = file1.read() == file2.read()
print(igual)

# Comparar los archivos

bool=filecmp.cmp('./Practica 1/ejemplos/data_file.txt', './copia.txt', shallow=False)
print(bool)

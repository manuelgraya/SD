"""9. Implemente la función get_file_info(filename) para que devuelva una
tupla con el tamaño en bytes del fichero, cuyo nombre se indica como
parámetro filename, en la primera posición, y una lista con las palabras
acabadas con el carácter 's' que contenga el fichero, en segunda posición.
Por ejemplo, la invocación get_file_info('mifichero.txt'), suponiendo
que 'mifichero.txt' contiene el texto “`La casa está pintada en muchos
colores'', devolverá la tupla (39, ['muchos', 'colores']). Si el
parámetro filename no es una cadena o es nulo (None) o si el fichero
indicado no existe, se deberá generar la excepción correspondiente."""

import os


def get_file_info(filename):
    if filename is None or not isinstance(filename,str):
        raise ValueError ("El nombre del fichero no puede ser nulo o no es una cadena")
    else:
        if os.path.exists(filename): #Si el fichero existe en la ruta indicada 
            with open(filename, 'r') as f: #Abre el fichero en modo lectura
                contenido = f.read() #Lee el contenido del fichero y lo guarda en la variable contenido
                palabras = contenido.split() #Divide el contenido en palabras y las guarda en la variable palabras
                palabras_s = [elemento for elemento in palabras if elemento.endswith('s')] #Guarda en la lista palabras_s las palabras que terminan en 's'
                return (os.path.getsize(filename), palabras_s)
        else:
            raise FileNotFoundError("El fichero no existe")
        
if __name__ == "__main__":
    ruta = "./SD/Practica 1/ejemplos/mifichero.txt"
    print(get_file_info(ruta))

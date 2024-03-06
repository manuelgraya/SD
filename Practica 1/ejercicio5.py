"""
Implemente la función list_add(mylist, e) para que añada el elemento e
a la lista mylist y devuelva la lista resultante. Por ejemplo, la invocación
de list_add([5, 2], 4) deberá devolver como resultado [5, 2, 4]. Si el
elemento es nulo (‘None’), se deberá generar la excepción
correspondiente.
"""

def list_add(mylist, e): #Función que añade un elemento a una lista
    if e is None: #Comprueba que el elemento no sea nulo
        raise ValueError ("El elemento no puede ser nulo") #Genera la excepción correspondiente
    else: #Si el elemento no es nulo, lo añade a la lista
        mylist.append(e) #Añade el elemento a la lista
        return mylist #Devuelve la lista resultante

def main():
        # Ejemplo 1
        mylist = [5, 2]
        e = 4
        resultado = list_add(mylist, e)
        print(f"La lista resultante es: {resultado}")

        # Ejemplo 2
        mylist = [3, 7]
        e = 'x'
        resultado = list_add(mylist, e)
        print(f"La lista resultante es: {resultado}")

        # Ejemplo 3
        mylist = [10, 15]
        e = 'cadena caracteres'
        resultado = list_add(mylist, e)
        print(f"La lista resultante es: {resultado}")

        # Ejemplo 4
        mylist = [10, 15]
        e = None
        resultado = list_add(mylist, e)
        print(f"La lista resultante es: {resultado}")

if __name__ == "__main__":
    main()

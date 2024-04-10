"""Implemente la función list_del(mylist, e) para que elimine la primera
ocurrencia del elemento e de la lista mylist y devuelva la lista resultante.
Por ejemplo, la invocación list_del([5, 2, 4], 2) deberá devolver como
resultado [5, 4]. Si el elemento es nulo (‘None’) o la lista mylist está
vacía, se deberá generar la o las excepciones correspondientes"""

def list_del(mylist, e): 
    if e is None:
        raise ValueError ("El elemento no puede ser nulo")
    elif len(mylist) == 0: #Comprueba que la lista no esté vacía
        raise ValueError ("La lista no puede estar vacía")
    else:
        mylist.remove(e) #Elimina el elemento de la lista

        return mylist #Devuelve la lista resultante
    
def main():
        # Ejemplo 1
        mylist = [5, 2, 4]
        e = 2
        resultado = list_del(mylist, e)
        print(f"La lista resultante es: {resultado}")

        # Ejemplo 2
        mylist = [3, 7]
        e = 3
        resultado = list_del(mylist, e)
        print(f"La lista resultante es: {resultado}")

        # Ejemplo 3
        mylist = [10, 15, 10]
        e = 10
        resultado = list_del(mylist, e)
        print(f"La lista resultante es: {resultado}")

        # Ejemplo 4
        mylist = [10, 15]
        e = None
        resultado = list_del(mylist, e)
        print(f"La lista resultante es: {resultado}")

if __name__ == "__main__":
    main()

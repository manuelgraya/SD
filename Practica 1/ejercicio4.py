def accum(x, y, z):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int): #Comprueba que los argumentos sean enteros
        raise TypeError("Los argumentos deben ser enteros") #Genera la excepción correspondiente y si hay un error sale del programa
    else:
        suma = 0
        if x%2 == 0:
            suma += x
        if y%2 == 0:
            suma += y
        if z%2 == 0:
            suma += z

        return suma
    
def main():
    try:
        # Ejemplo 1
        x = 5
        y = 4
        z = 2
        resultado = accum(x, y, z)
        print(f"La suma de los números pares es: {resultado}")

        # Ejemplo 2
        x = 3
        y = 's'
        z = 9
        resultado = accum(x, y, z)
        print(f"La suma de los números pares es: {resultado}")

        # Ejemplo 3
        x = 10
        y = 15
        z = 20
        resultado = accum(x, y, z)
        print(f"La suma de los números pares es: {resultado}")

    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

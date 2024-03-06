"""8. Implemente la función prime(a, b) para que devuelva una lista con los
números primos en el intervalo cerrado [a, b]. Por ejemplo, la invocación
prime(2, 10) deberá devolver como resultado [2, 3, 5, 7]. Si los
parámetros a o b no son enteros o son nulos (None), se deberá generar la o
las excepciones correspondientes.
"""
def prime (a,b):
    
    if a is None or b is None or not isinstance (a, int) or not isinstance(b, int): #Si a o b son nulos o no son enteros
        raise ValueError ("Los parámetros a y b no pueden ser nulos o no son enteros")
    else:
        primos = []
        for i in range(a,b+1):
            if i > 1:
                for j in range(2,i//2+1):
                    if i % j == 0: #Si el residuo de la división de i entre j es 0, no es primo
                        break
                else:
                    primos.append(i)
    return primos
    
def main():
    print(prime(1,1000))

if __name__ == "__main__":
    main()
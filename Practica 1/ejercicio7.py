"""7. Implemente la función dict_add(mydict, t) para que añada la tupla
(clave, valor) t pasada por parámetro al diccionario mydict. Por ejemplo,
la invocación dict_add({1: 'manzana'}, (2, 'fresa')) deberá devolver
como resultado {1: 'manzana', 2: 'fresa'}. Si el elemento t es nulo
(None) o no es una tupla de dos elementos, se deberá generar la o las
excepciones correspondientes.
"""
#tupla = (2, 'fresa')
# ___ = ___.copy() para copiar lista y no modificar su valor

def dict_add(mydict, t):
    if t is None or not isinstance(t,tuple) or len(t) != 2:
        raise ValueError ("El elemento no puede ser nulo o no es una tupla de elementos")
    else:
        mydict = mydict.copy()
        mydict[t[0]] = t[1]
        #mydict.append(t[0], t[1])
        return mydict

def main():
        # Ejemplo 1
        mydict = {1: 'manzana'}
        t = (2, 'platano')
        resultado = dict_add(mydict, t)
        print(f"El diccionario resultante es: {resultado}")

        # Ejemplo 2
        mydict = {3: 'naranja'}
        t = (4, 'pera', 'plátano')
        resultado = dict_add(mydict, t)
        print(f"El diccionario resultante es: {resultado}")

        # Ejemplo 3
        mydict = {10: 'melocotón'}
        t = None
        resultado = dict_add(mydict, t)
        print(f"El diccionario resultante es: {resultado}")

if __name__ == "__main__":
    main()
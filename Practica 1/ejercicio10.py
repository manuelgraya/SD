"""Implemente una función en Python que realice la intersección de dos
listas. Tenga en cuenta que no puede haber elementos repetidos."""

def interseccion(lista1, lista2):
    return list(set(lista1) & set(lista2))
    

if __name__ == "__main__":
    lista1 = [1,2,3,4,5]
    lista2 = [3,4,5,6,7]
    print(interseccion(lista1, lista2))
    lista1 = [1,2,3,4,5]
    lista2 = [6,7,8,9,10]
    print(interseccion(lista1, lista2))
    lista1 = [1,2,3,4,5]
    lista2 = [1,2,3,4,5]
    print(interseccion(lista1, lista2))
    lista1 = [1,2,3,4,5]
    lista2 = [5,4,3,2,1]
    print(interseccion(lista1, lista2))
    lista1 = [1,2,3,4,5]
    lista2 = [1,2,3,4,5,6,7,8,9,10]
    print(interseccion(lista1, lista2))
    lista1 = [1,2,3,4,5,6,7,8,9,10]
    lista2 = [1,2,3,4,5]
    print(interseccion(lista1, lista2))
    lista1 = [1,2,3,4,5,6,7,8,9,10]
    lista2 = [6,7,8,9,10]
    print(interseccion(lista1, lista2))
    lista1 = [1,2,3,4,5,6,7,8,9,10]
    lista2 = [1,2,3,4,5,6,7,8,9,10]
    print(interseccion(lista1, lista2))
    lista1 = [1,2,3,4,5,6,7,8,9,10]
    lista2 = [10,9,8,7,6,5,4,3,2,1]
    print(interseccion(lista1, lista2))
    lista1 = [1,2,3,4,5,6,7,8,9,10]
    lista2 = [10,9,8,7,6,5,4,3,2,1,11,12,13,14,15]
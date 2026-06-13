def interschimb(a, b):
    a = a + b
    b = a - b
    a = a - b

    return a, b

def interschimbCuLista(lista):
    lista[0], lista[1] = lista[1], lista[0]


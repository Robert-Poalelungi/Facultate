def interschimb(a, b):
    local = a
    a = b
    b = local
    return None

def interschimb_list(lista):
    local = lista[0]
    lista[0] = lista[1]
    lista[1] = local



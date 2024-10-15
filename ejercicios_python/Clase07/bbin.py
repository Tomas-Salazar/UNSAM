def donde_insertar(lista, x):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            return medio
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return izq

def insertar(lista, x):
    pos = donde_insertar(lista, x)
    if pos < len(lista) and lista[pos] == x:
        return pos
    lista.insert(pos, x)
    return pos
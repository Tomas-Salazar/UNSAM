def busqueda_lineal_ordenada(lista, e):
    '''Si e está en la lista ordenada devuelve su posición, de lo
    contrario devuelve -1. Se detiene si encuentra un valor mayor que e.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z > e:   # si encontramos un elemento mayor que e
            break   # salimos del ciclo, no hay necesidad de continuar
        if z == e:  # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos
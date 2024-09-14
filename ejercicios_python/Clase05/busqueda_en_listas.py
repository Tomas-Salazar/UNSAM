# Ejercicio 5.3: Búsquedas de un elemento


def buscar_u_elemento(lista, elemento):
    lista = lista[::-1]
    if elemento in lista:
        indice = lista.index(elemento)
        return f'El índice del último elemento en la lista es la {indice}.'
    else:
        indice = -1
        return f'El índice del elemento en la lista es la {indice} ya que no se encuentra.'


rango = [0,1,5,8,2,8,3,8,0,21,5,3,4,0,5]
numero1 = 0
numero2 = 9
print(buscar_u_elemento(rango, numero1))
print(buscar_u_elemento(rango, numero2))


def buscar_n_elemento(lista, elemento):
    cantidad = 0
    for i in lista:
        if i == elemento:
            cantidad += 1
        else:
            pass
    return f'El elemento se encontro {cantidad} veces en la lista'


print(buscar_n_elemento(rango, numero1))



# Ejercicio 5.4: Búsqueda de máximo y mínimo

# La corrección fue inicializar el m en None en lugar de 0, debido a que iniciarlizarlo en 0 trae problemas ya que 0 ya condiciona porque es mayor que los negativos
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = None # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if m == None:
            m = e
        elif e > m:
            m = e
        else:
            pass
    return m


def minimo(lista):
    m = None
    for e in lista:
        if m == None:
            m = e
        elif e < m:
            m = e
        else:
            pass
    return m


# print(maximo(rango))
print(maximo([1,2,7,2,3,4]), minimo([1,2,7,2,3,4]))

print(maximo([1,2,3,4]), minimo([1,2,3,4]))

print(maximo([-5,4]), minimo([-5,4]))

print(maximo([-5,-4]), minimo([-5,-4,-6]))
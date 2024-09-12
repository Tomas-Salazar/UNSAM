# Ejercicio 5.3: Búsquedas de un elemento

def buscar_u_elemento(lista, elemento):
    lista = lista[::-1]
    if elemento in lista:
        
        indice = lista.index(elemento)
        print(f'La índice del último elemento en la lista es la {indice}.')
    else:
        print(f'El índice del elemento es -1 ya que no se encuentra en la lista.')

rango = [0,1,5,8,2,8,3,8,0,21,5,3,4,0,5]
numero = 0
print(buscar_u_elemento(rango, numero))
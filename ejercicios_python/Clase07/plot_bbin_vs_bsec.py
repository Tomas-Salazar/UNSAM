import random
import matplotlib.pyplot as plt
import numpy as np

def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos

def busqueda_secuencial_comps(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


m = 10000
k = 1000

# largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
# comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

# for i, n in enumerate(largos):
#     lista = generar_lista(n, m) # genero lista de largo n
#     comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

# # ahora grafico largos de listas contra operaciones promedio de búsqueda.
# plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
# plt.xlabel("Largo de la lista")
# plt.ylabel("Cantidad de comparaciones")
# plt.title("Complejidad de la Búsqueda")
# plt.legend()
# plt.show()

################### Ejercicio 7.17: Búsqueda binaria vs. búsqueda secuencial

def busqueda_binaria_comps(lista, x):
    comps = 0
    izq, der = 0, len(lista) - 1
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if lista[medio] == x:
            return medio, comps
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return -1, comps

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista, x)[1]
    
    comps_prom = comps_tot / k
    return comps_prom

def graficar_bbin_vs_bseq(m, k):
    largos = np.arange(1, 257)
    comps_promedio_sec = np.zeros(256)
    comps_promedio_bin = np.zeros(256)
    
    for i, n in enumerate(largos):
        lista = generar_lista(n, m)
        # B secuencial
        comps_promedio_sec[i] = experimento_secuencial_promedio(lista, m, k)
        # B binaria
        comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)
    
    plt.plot(largos, comps_promedio_sec, label='Búsqueda Secuencial')
    plt.plot(largos, comps_promedio_bin, label='Búsqueda Binaria')
    
    plt.xlabel("Largo de la lista")
    plt.ylabel("Comparaciones promedio")
    plt.title("Búsqueda Secuencial vs Búsqueda Binaria")
    plt.legend()
    plt.show()

graficar_bbin_vs_bseq(m, k)
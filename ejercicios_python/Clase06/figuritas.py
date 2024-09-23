import numpy as np
import random

"""
Datos:
Álbum con 670 figuritas.
Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
Cada paquete tiene cinco figuritas.
"""

# Ejercicio 6.13: Crear
def crear_album(figus_total):
    album = np.zeros(figus_total).astype(int)
    return album


# Ejercicio 6.14: Incompleto
def album_incompleto(A):
    comprobacion = True if 0 in A else False
    # Otra forma es comprobacion = np.any(A == 0)
    return comprobacion


# Ejercicio 6.15: Comprar
def comprar_figu(figus_total):
    indice_figu = random.randint(1, figus_total)
    return indice_figu


# Ejercicio 6.16: Cantidad de compras
def cuantas_figus(figus_total):
    figus_compradas = 0
    album = crear_album(figus_total)
    
    while album_incompleto(album):
        indice_figu = comprar_figu(figus_total)
        album[indice_figu-1] += 1
        figus_compradas += 1
    
    return figus_compradas


# Ejercicio 6.17:
def calcular_promedio(repeticiones, figus_total):    # experimento_figus()
    lista_resultados = [cuantas_figus(figus_total) for _ in range(repeticiones+1)]
    
    return round(np.mean(lista_resultados), 2)

n_repeticiones = 1000
figus_total = 6
promedio_6_en_1000 = calcular_promedio(n_repeticiones, figus_total)
# print(promedio_6_en_1000)


# Ejercicio 6.18: 
# experimento_figus(n_repeticiones, figus_total) ya realizado en 6.17(pense que me pedían eso)
n_repeticiones = 100
figus_total = 670
promedio_670_en_100 = calcular_promedio(n_repeticiones, figus_total)
print(promedio_670_en_100)
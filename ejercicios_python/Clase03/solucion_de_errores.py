#solucion_de_errores.py
#Ejercicios de errores en el código


#%%
# Ejercicio 3.5: Semántica
# ¿Anda bien en todos los casos de prueba? 
# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         else:
#             return False
#         i += 1

#Comentario: El error era del tipo Semántico y era principalmente los return, que el return finaliza abruptamente el ciclo.
#    Lo corregí sacando los return y modificando el código, cosa de que si se cumple el if, me incremente una variable que me 
#    indica cuántas letras "a" encontró e informarlo cualquiera sea el caso.

#    A continuación va el código corregido
# def correccion_tiene_a(expresion):
#     n = len(expresion)
#     letras = 0
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             letras += 1
#         else:
#             pass
#         i += 1
#     print(f'La expresión tiene {letras} letras "a".')

# tiene_a('UNSAM 2020')
# tiene_a('abracadabra')
# tiene_a('La novela 1984 de George Orwell')


#%%
# Ejercicio 3.6: Sintaxis
# ¿Anda bien en todos los casos de prueba?
# def tiene_a(expresion)
#     n = len(expresion)
#     i = 0
#     while i<n
#         if expresion[i] = 'a'
#             return True
#         i += 1
#     return Falso

#Comentario: El error era del tipo Sintaxis, mala escritura en el código, faltan los "dos puntos" en el def, en el while,
# en el if, además la comparación '==' eran en realidad una asignación '=', y por último 'False' estaba escrito como 'Falso'
#    Se corrigió con lo recién mencionado como incorrecto poniendolo de forma correcta y corrigiendo también los pasados errores 
#    semánticos de la función anterior

#    A continuación va el código corregido
# def correccion_tiene_a(expresion):
#     n = len(expresion)
#     letras = 0
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             letras += 1
#         else:
#             pass
#         i += 1
#     print(f'La expresión tiene {letras} letras "a".')

# tiene_a('UNSAM 2020')
# tiene_a('La novela 1984 de George Orwell')


#%%
# Ejercicio 3.7: Tipos
# ¿Anda bien en todos los casos de prueba?
# def tiene_uno(expresion):
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#         i += 1
#     return tiene

#Comentario: El error era del tipo 'tiempo de ejecución' y se debía que la funcion no estaba preparada para manipular objetos
# del tipo int, por eso arrojaba error al recibir por parámetro como argumento un int
#    Lo corregí modificando el código, cosa de que pueda manejar strings, se podría mejorar añadiendo estructuras de manejo de errores

#    A continuación va el código corregido
# def tiene_uno(expresion):
#     expresion_str = str(expresion)
#     n = len(expresion_str)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion_str[i] == '1':
#             tiene = True
#         i += 1
#     return tiene

# tiene_uno('UNSAM 2020')
# tiene_uno('La novela 1984 de George Orwell')
# tiene_uno(1984)


#%%
# Ejercicio 3.8: Alcances
# La siguiente suma no da lo que debería:
# def suma(a,b):
#     c = a + b

# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")

#Comentario: El error era del tipo Sintaxis, únicamente lo que le faltaba a la función era retornar la variable donde se guardó la suma
#    Lo corregí agregándoselo

#    A continuación va el código corregido
# def suma(a,b):
#     c = a + b
#     return c

# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")


#%%
# Ejercicio 3.9: Pisando memoria
# El siguiente ejemplo usa el dataset de la clase anterior, pero no lo imprime como corresponde, 
# ¿podés determinar por qué y explicarlo brevemente en la versión corregida?
import csv
from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt", encoding='utf8') as file:
#         filas = csv.reader(file)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

# camion = leer_camion('ejercicios_python/Data/camion.csv')
# pprint(camion)


#Comentario: El error era del tipo Semántico y se debía a que el diccionario que se completaba era siempre el mismo, lo que se buscaba era
# poder llenar la lista con muchos diccionarios diferentes, y no era lo que estaba ocurriendo
#    Lo corregí modificando el código, cosa de que en cada iteracion se cree un nuevo diccionario con su propias
#    claves y valores y ese sea el que complete la lista

#    A continuación va el código corregido
def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt", encoding='utf8') as file:
        filas = csv.reader(file)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('ejercicios_python/Data/camion.csv')
pprint(camion)
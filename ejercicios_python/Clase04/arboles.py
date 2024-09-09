import csv
from pprint import pprint
from collections import Counter

archivo_arboles = 'ejercicios_python/Data/arbolado-en-espacios-verdes.csv'


# Ejercicio 4.13: Lectura de los árboles de un parque
def leer_parque(nombre_archivo, nombre_parque = None):
    lista_arboles = []
    # long	lat	id_arbol	altura_tot	diametro	inclinacio	id_especie	nombre_com	nombre_cie	
    # tipo_folla	espacio_ve	ubicacion	nombre_fam	nombre_gen	origen	coord_x	coord_y
    
    with open(nombre_archivo, 'rt', encoding='utf8') as file:
        rows = csv.reader(file)
        headers = next(rows)
        
        for i, row in enumerate(rows, start=1):
            try:
                dict_arbol = dict(zip(headers, row))
                dict_arbol['long'] = float(dict_arbol['long'])
                dict_arbol['lat'] = float(dict_arbol['lat'])
                dict_arbol['id_arbol'] = int(dict_arbol['id_arbol'])
                dict_arbol['altura_tot'] = float(dict_arbol['altura_tot'])
                dict_arbol['diametro'] = int(dict_arbol['diametro'])
                dict_arbol['inclinacio'] = int(dict_arbol['inclinacio'])
                dict_arbol['id_especie'] = int(dict_arbol['id_especie'])
                dict_arbol['nombre_com'] = str(dict_arbol['nombre_com'])
                dict_arbol['nombre_cie'] = str(dict_arbol['nombre_cie'])
                dict_arbol['tipo_folla'] = str(dict_arbol['tipo_folla'])
                dict_arbol['espacio_ve'] = str(dict_arbol['espacio_ve'])
                dict_arbol['ubicacion'] = str(dict_arbol['ubicacion'])
                dict_arbol['nombre_fam'] = str(dict_arbol['nombre_fam'])
                dict_arbol['nombre_gen'] = str(dict_arbol['nombre_gen'])
                dict_arbol['origen'] = str(dict_arbol['origen'])
                dict_arbol['coord_x'] = float(dict_arbol['coord_x'])
                dict_arbol['coord_y'] = float(dict_arbol['coord_y'])
                
                if nombre_parque is None or dict_arbol['espacio_ve'] == nombre_parque:
                    lista_arboles.append(dict_arbol)
            except ValueError:
                    print('Faltan datos en la línea', i, 'del archivo.')
    return lista_arboles


# Ejercicio 4.14: Determinar las especies en un parque
def obtener_especies(lista_arboles):
    lista_especies = [i['nombre_com'] for i in lista_arboles]
    conjunto_especies = set(lista_especies)
    return conjunto_especies


# Ejercicio 4.15: Contar ejemplares por especie
def contar_ejemplares(lista_arboles):
    lista_especies = [i['nombre_com'] for i in lista_arboles]
    contador_especies = Counter(lista_especies)
    return contador_especies


def especies_mas_comunes(nombre_archivo, nombre_parque):
    arboles = leer_parque(nombre_archivo, nombre_parque)
    contador = contar_ejemplares(arboles)
    contador_mas_comunes = contador.most_common(5)
    return contador_mas_comunes


# Ejercicio 4.16: Alturas de una especie en una lista
def obtener_alturas(lista_arboles, especie):
    lista_alturas = []
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            lista_alturas.append(i['altura_tot'])
    # lista_alturas = [i['altura_tot'] for i['nombre_com'] == especie in lista_arboles]
    return lista_alturas


def max_mean_altura(lista_arboles, nombre_especie):
    lista_alturas = obtener_alturas(lista_arboles, nombre_especie)
    altura_max = max(lista_alturas)
    altura_mean = sum(lista_alturas) / len(lista_alturas)
    return altura_max, altura_mean


# Ejercicio 4.17: Inclinaciones por especie de una lista
def obtener_inclinaciones(lista_arboles, especie):
    lista_inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista_inclinaciones.append((arbol['nombre_com'], arbol['inclinacio']))
    return lista_inclinaciones


# Ejercicio 4.18: Especie con el ejemplar más inclinado
def ejemplar_mas_inclinado(lista_arboles, nombre_especie):
    lista_inclinaciones = obtener_inclinaciones(lista_arboles, nombre_especie)
    
    inclinacion_maxima = 0
    especie_mas_inclinada = None
    for especie, inclinacion in lista_inclinaciones:
        if inclinacion > inclinacion_maxima:
            inclinacion_maxima = inclinacion
            especie_mas_inclinada = especie
    return especie_mas_inclinada, inclinacion_maxima


# Ejercicio 4.19: Especie más inclinada en promedio
def ejemplar_promedio_mas_inclinada(lista_arboles, especie):
    pass


parque = 'EL ROSEDAL (Sector dentro de Plaza HOLANDA)'
arboles = leer_parque(archivo_arboles, parque)
# pprint(arboles)

# especies_unicas = obtener_especies(arboles)
# print(especies_unicas)

parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
# contador = contar_ejemplares(arboles)
# for parque in parques:                                # Corresponde al ejercicio 4.15
#     especies_comunes = especies_mas_comunes(archivo_arboles, parque)
#     for especie, cantidad in especies_comunes:
#         print(f'Nombre parque: {parque:<20}Nombre especie: {especie:<25}Numero de especies: {cantidad:<20}')
#     print()

especie = 'Jacarandá'
# for parque in parques:                                  # Corresponde al ejercicio 4.16
#     listas_arboles = leer_parque(archivo_arboles, parque)
#     max_arboles, mean_arboles = max_mean_altura(listas_arboles, especie)
#     print(f'Nombre parque: {parque:<20}Arbol más alto: {max_arboles:<25.2f}Promedio de altura: {mean_arboles:<20.2f}')

# for parque in parques:                                  # Corresponde al ejercicio 4.17
#     listas_arboles = leer_parque(archivo_arboles, parque)
#     inclinaciones = obtener_inclinaciones(listas_arboles, especie)
#     print(f'Nombre parque: {parque:<20s}Nombre especie: {especie:<25s}Inclinaciones: {inclinaciones}')

for parque in parques:                                    # Corresponde al ejercicio 4.18
    listas_arboles = leer_parque(archivo_arboles, parque)
    especie_inclinada, inclinacion = ejemplar_mas_inclinado(listas_arboles, especie)
    print(f'Nombre parque: {parque:<20}Especie más inclinada: {especie_inclinada:<25}Inclinación: {inclinacion:<20.2f}')
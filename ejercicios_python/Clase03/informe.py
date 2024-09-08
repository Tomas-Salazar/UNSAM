# Informe
import csv
from pprint import pprint

archivo_camion = 'ejercicios_python/Data/camion.csv'
archivo_precios = 'ejercicios_python/Data/precios.csv'


def leer_camion(nombre_archivo):
    lista_camion = []
    
    file = open(nombre_archivo, 'rt')
    rows = csv.reader(file)
    _ = next(rows)
    
    for i, row in enumerate(rows):
        try:
            dict_lote = {}
            dict_lote['nombre'] = row[0]
            dict_lote['cajones'] = int(row[1])
            dict_lote['precio'] = float(row[2])
            lista_camion.append(dict_lote)
        except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    file.close()
    return lista_camion


def leer_precios(nombre_archivo):
    dict_precios = {}
    
    file = open(nombre_archivo, 'r', encoding='utf8')
    rows = csv.reader(file)
    for i, row in enumerate(rows):
        try:
            if row:
                dict_precios[ row[0].capitalize() ] = float(row[1])
        except:
                print(f'Algo ocurrió con la línea {i}')
    return dict_precios


camion = leer_camion(archivo_camion)
total = 0
for i in camion:
    total += i['cajones'] * i['precio']
print(f'Costo total: $ {total}')
# pprint(camion)

precios = leer_precios(archivo_precios)
# pprint(precios)

suma_ventas = 0
for k, v in precios.items():
    for i in camion:
        if k.capitalize() == i['nombre'].capitalize():
            suma_ventas += i['cajones'] * v
        else:
            pass
print('Las ventas totales fueron de: $', suma_ventas)

balance = (suma_ventas - total)

print('El balance total recaudado es de: $', round(balance, 2))

#---
print("********************************")
precios_invertidos = list(zip(precios.values(), precios.keys()))
# [('Pera', 490.1), ('Lima', 23.45), ('Naranja', 91.1), ('Mandarina', 34.23)]
print(precios_invertidos)
# Informe
import csv
from pprint import pprint

# archivo_camion = 'ejercicios_python/Data/camion.csv'
archivo_precios = 'ejercicios_python/Data/precios.csv'
archivo_fechas = 'ejercicios_python/Data/fecha_camion.csv'


def leer_camion(nombre_archivo):
    lista_camion = []
    
    with open(nombre_archivo, 'rt', encoding='utf8') as file:
        rows = csv.reader(file)
        headers = next(rows)
        
        for i, row in enumerate(rows, start=1):
            try:
                dict_lote = dict(zip(headers, row))
                dict_lote['cajones'] = int(dict_lote['cajones'])
                dict_lote['precio'] = float(dict_lote['precio'])
                lista_camion.append(dict_lote)
            except ValueError:
                    print('Faltan datos en la línea', i, 'del archivo.')
    return lista_camion


def leer_precios(nombre_archivo):
    dict_precios = {}
    
    with open(nombre_archivo, 'rt', encoding='utf8') as file:
        rows = csv.reader(file)
        for i, row in enumerate(rows):
            try:
                if row:
                    dict_precios[ row[0].capitalize() ] = float(row[1])
            except:
                    print(f'Algo ocurrió con la línea {i}')
    return dict_precios


camion = leer_camion(archivo_fechas)
total = 0
for i in camion:
    total += i['cajones'] * i['precio']
print(f'Costo total: $ {total}')
# pprint(camion)

precios = leer_precios(archivo_precios)
suma_ventas = 0
for k, v in precios.items():
    for i in camion:
        if k.capitalize() == i['nombre'].capitalize():
            suma_ventas += i['cajones'] * v
        else:
            pass
print('Las ventas totales fueron de: $', suma_ventas)
# pprint(precios)

balance = (suma_ventas - total)
print('El balance total recaudado es de: $', round(balance, 2))
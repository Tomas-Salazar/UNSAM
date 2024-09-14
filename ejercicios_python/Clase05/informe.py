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
# total = 0
# for i in camion:
#     total += i['cajones'] * i['precio']
total = sum([i['cajones'] * i['precio'] for i in camion])
print(f'Costo total: $ {total}')
# pprint(camion)

precios = leer_precios(archivo_precios)
# suma_ventas = 0
# for k, v in precios.items():
#     for i in camion:
#         if k.capitalize() == i['nombre'].capitalize():
#             suma_ventas += i['cajones'] * v
#         else:
#             pass
suma_ventas = sum([i['cajones'] * precios[i['nombre']] for i in camion])
print('Las ventas totales fueron de: $', suma_ventas)
# pprint(precios)

balance = (suma_ventas - total)
print('El balance total recaudado es de: $', round(balance, 2))


# Ejercicio 5.9: Consultas de datos
mas100 = [i for i in camion if i['cajones'] > 100]
print(mas100)

myn = [i for i in camion if i['nombre'] in {'Mandarina', 'Naranja'}]
print(myn)

costo10k = [i for i in camion if i['cajones']*i['precio'] > 10000]
print(costo10k)


# Ejercicio 5.10: Extracción de datos
# nombre_cajones =[(s['nombre'], s['cajones']) for s in camion]
# nombre_cajones
# [('Lima', 100), ('Naranja', 50), ('Caqui', 150), ('Mandarina', 200), ('Durazno', 95), ('Mandarina', 50), ('Naranja', 100)]
    # Si cambiamos corchetes por llaves, tenemos una comprensión de conjuntos
    # Si usamos clave:valor obtendríamos una comprensión de diccionarios


# Ejercicio 5.11: Extraer datos de un archivo CSV

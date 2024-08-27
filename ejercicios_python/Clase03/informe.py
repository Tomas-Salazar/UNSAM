# Informe
import csv
from pprint import pprint

archivo = 'ejercicios_python/Data/camion.csv'


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


def calcular_costo_total(lista_dict):
    total = 0
    
    for i in lista_dict:
        total += i['cajones'] * i['precio']
    return f'Costo total: $ {total}'


camion = leer_camion(archivo)
pprint(camion)
print(calcular_costo_total(camion))
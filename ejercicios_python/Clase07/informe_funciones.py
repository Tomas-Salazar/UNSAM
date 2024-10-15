# Tabla Informe
import csv
from fileparse import parse_csv

archivo_camion = 'ejercicios_python/Data/camion.csv'
archivo_precios = 'ejercicios_python/Data/precios.csv'


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


def hacer_informe(lista, precios):
    # Convertir la lista de tuplas (precios) a un diccionario
    precios_dict = dict(precios)
    
    informe = []
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    
    for i in lista:
        nombre = i['nombre']
        cajones = i['cajones']
        precio_compra = i['precio']
        precio_venta = precios_dict.get(nombre, 0)
        cambio = precio_venta - precio_compra
        informe.append((nombre, cajones, precio_compra, cambio))
    
    encabezado = ' '.join([f'{header:>10}' for header in headers])
    print(encabezado)
    
    division = ' '.join(['-'*10 for _ in headers])
    print(division)
    
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {"$"+str(precio):>10s} {cambio:>10.2f}')
    
    return informe


def informe_camion(archivo_camion, archivo_precios):
    camion = parse_csv(archivo_camion, types=[str, int, float])
    precios = parse_csv(archivo_precios, types=[str,float], has_headers=False)
    hacer_informe(camion, precios)

# informe_camion(archivo_camion, archivo_precios)

# files = [archivo_camion, archivo_camion]
# for name in files:
#     print(f'{name:-^43s}')
#     informe_camion(name, 'ejercicios_python/Data/precios.csv')
#     print()
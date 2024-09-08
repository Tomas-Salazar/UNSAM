# Tabla Informe
import csv
from pprint import pprint

archivo_camion = 'ejercicios_python/Data/camion.csv'
archivo_precios = 'ejercicios_python/Data/precios.csv'
# archivo_fechas = 'ejercicios_python/Data/fecha_camion.csv'


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


def hacer_informe(lista, dicc):
    informe = []
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio') # Se puede modificar y pasar por parámetros o bien creando otra función, más módulos
    
    for i in lista:
        nombre = i['nombre']
        cajones = i['cajones']
        precio_compra = i['precio']
        precio_venta = dicc.get(nombre, 0)  # En caso de no existir 'nombre' se asigna 0, ya que si no existe arroja un error.
        cambio = precio_venta - precio_compra
        informe.append((nombre, cajones, precio_compra, cambio))
    
    encabezado = ' '.join([f'{header:>10}' for header in headers])
    print(encabezado)
    
    division = ' '.join(['-'*10 for _ in headers])
    print(division)
    
    return informe


camion = leer_camion(archivo_camion)
# total = 0
# for i in camion:
#     total += i['cajones'] * i['precio']
# print(f'Costo total: $ {total}')
# # pprint(camion)

precios = leer_precios(archivo_precios)
# suma_ventas = 0
# for k, v in precios.items():
#     for i in camion:
#         if k.capitalize() == i['nombre'].capitalize():
#             suma_ventas += i['cajones'] * v
#         else:
#             pass
# print('Las ventas totales fueron de: $', suma_ventas)
# # pprint(precios)

# balance = (suma_ventas - total)
# print('El balance total recaudado es de: $', round(balance, 2))

informe = hacer_informe(camion, precios)
for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {"$"+str(precio):>10s} {cambio:>10.2f}')
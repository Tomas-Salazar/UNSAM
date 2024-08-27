# Buscar Precios
import csv
from pprint import pprint

archivo = 'ejercicios_python/Data/precios.csv'


def buscar_precio(nombre_archivo, fruta):
    data = open(nombre_archivo, 'rt', encoding='utf8')
    encontrado = False
    try:
        for line in data:
            row = line.split(',')
            if row[0].lower() == fruta.lower():
                print(f'El precio de un cajón de {fruta.capitalize()} es: ',float(row[1].strip()) )
                encontrado = True
                break
        if not encontrado:
            print(fruta.capitalize(), 'no figura en el listado de precios.')
    finally:
        data.close()


buscar_precio(archivo, 'frambuesa')
buscar_precio(archivo, 'kale')


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


# pprint(leer_precios(archivo))
precios = leer_precios(archivo)
# pprint(precios)

print(precios['Naranja'])
print(precios['Mandarina'])
print(precios['Kiwi'] if 'Kiwi' in precios else 'no se encontró la fruta solicitada')
print(precios['Banana']  if 'Banana' in precios else 'no se encontró la fruta solicitada')
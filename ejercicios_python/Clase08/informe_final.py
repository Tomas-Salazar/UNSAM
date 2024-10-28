import sys
from fileparse import parse_csv

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as file:
        camion = parse_csv(file, select=['nombre', 'cajones', 'precio'], types=[str, int, float], has_headers=True, silence_errors=True)
    return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as file:
        precios = parse_csv(file, types=[str, float], has_headers=False, silence_errors=True)
        # Convertir la lista de tuplas a diccionario
        return dict((producto.capitalize(), precio) for producto, precio in precios)


def hacer_informe(lista, precios):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    informe = []
    
    for lote in lista:
        nombre = lote['nombre']
        cajones = lote['cajones']
        precio_compra = lote['precio']
        precio_venta = precios.get(nombre.capitalize(), 0.0)
        cambio = precio_venta - precio_compra
        informe.append((nombre, cajones, precio_compra, cambio))
    
    # Imprimir el informe
    encabezado = ' '.join([f'{header:>10}' for header in headers])
    print(encabezado)
    print('-' * len(encabezado))
    
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {"$"+str(precio):>10s} {cambio:>10.2f}')
    
    return informe


def informe_camion(archivo_camion='ejercicios_python/Data/camion.csv', archivo_precios='ejercicios_python/Data/precios.csv'):
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    return hacer_informe(camion, precios)


def main(params):
    archivo_camion = params[1] if len(params) > 1 else 'ejercicios_python/Data/camion.csv'
    archivo_precios = params[2] if len(params) > 2 else 'ejercicios_python/Data/precios.csv'
    informe_camion(archivo_camion, archivo_precios)


if __name__ == '__main__':
    main(sys.argv)
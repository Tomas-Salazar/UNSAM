# fileparse.py
import csv

archivo_camion = 'ejercicios_python/Data/camion.csv'
archivo_precios = 'ejercicios_python/Data/precios.csv'


def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo, encoding='utf8') as f:
        filas = csv.reader(f)
        if has_headers:
            # Lee los encabezados del archivo
            encabezados = next(filas)
            
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
            
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
                
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                registros.append(tuple(fila))
    return registros

# camion = parse_csv(archivo_camion)
# print(camion)

# cajones_retenidos = parse_csv(archivo_camion, types=[str, int, float])
# print(cajones_retenidos)

# cajones_lote = parse_csv(archivo_camion, select=['nombre', 'cajones'], types=[str, int])
# print(cajones_lote)

precios = parse_csv(archivo_precios, types=[str,float], has_headers=False)
print(precios)
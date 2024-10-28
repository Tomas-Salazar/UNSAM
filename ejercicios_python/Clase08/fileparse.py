import csv
import gzip

archivo_camion = 'ejercicios_python/Data/camion.csv'
archivo_precios = 'ejercicios_python/Data/precios.csv'
archivo_faltantes = 'ejercicios_python/Data/missing.csv'


def parse_csv(objeto_iterable, select=None, types=None, has_headers=True, silence_errors=False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    No olvidar elegir el tipo de datos de las columnas, y que si no se seleccionan columnas, settear has_headers en False.
    En caso de querer leer los reportes de errores, settear silence_errors en True
    '''
    # Verificación de la combinación inválida de select y has_headers=False
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    
    # Lee el objeto_iterable directamente (en lugar de abrir un archivo)
    filas = csv.reader(objeto_iterable)
    
    if has_headers:
        # Lee la primera fila como encabezados
        encabezados = next(filas)
        
        # Si existe 'select', se seleccionan los índices de las columnas solicitadas
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select  # Los encabezados ahora solo contienen las columnas seleccionadas
        else:
            indices = []
            
        registros = []
        
        # Procesa cada fila de datos junto con su índice
        for i, fila in enumerate(filas, start=1):
            if not fila:  # Saltea filas vacías
                continue
            # Si existen índices, filtra la fila según los índices de columnas seleccionadas
            if indices:
                fila = [fila[index] for index in indices]
            
            # Intenta convertir los datos en el tipo especificado (si se proporciona 'types')
            try:
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                # Arma diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            
            # Si hay un error de conversión, reporta el error y la fila, y la omite
            except ValueError as e:
                # Imprime advertencia solo si silence_errors es False
                if not silence_errors:
                    print(f'Advertencia: Fila {i} no pudo ser procesada. Motivo: {e}')
    else:
        registros = []
        # Procesa cada fila como una tupla si no hay encabezados
        for i, fila in enumerate(filas, start=1):
            if not fila:  # Saltea filas vacías
                continue
            try:
                # Aplica conversión de tipos si está especificado types
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                # Agrega la fila como tupla al resultado final
                registros.append(tuple(fila))
            
            # Captura y reporta errores de conversión
            except ValueError as e:
                # Imprime advertencia solo si silence_errors es False
                if not silence_errors:
                    print(f'Advertencia: Fila {i} no pudo ser procesada. Motivo: {e}')
    return registros


# Ejemplos ejercicio 8.1
# precios = parse_csv(archivo_precios, types=[str,float], has_headers=False)                                            # No tira error
# print(precios)

# cajones_lote = parse_csv(archivo_camion, select=['nombre', 'cajones'], types=[str, int], has_headers=False)           # Tira error
# print(cajones_lote)

# Ejemplo ejercicio 8.2, 8.3
# mas_frutas = parse_csv(archivo_faltantes, types=[str,int], has_headers=True, select=['nombre', 'cajones'])
# print(mas_frutas)

# Ejemplos ejercicio 8.7
# with gzip.open('ejercicios_python/Data/camion.csv.gz', 'rt') as file:                             # Funciona bien
#     camion = parse_csv(file, types=[str,int,float])
# print(camion)

# lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']       # Funciona bien
# camion2 = parse_csv(lines, types=[str,int,float])
# print(camion2)

# camion2 = parse_csv(archivo_camion, types=[str,int,float])                                        # Funciona mal
# print(camion2)
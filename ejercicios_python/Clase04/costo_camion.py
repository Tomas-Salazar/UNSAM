# Ejercicios 4.4
import csv


def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf8') as file:
        rows = csv.reader(file)
        headers = next(rows)
        total = 0
        for row in enumerate(rows, start=1):
            record = dict(zip(headers, row[1]))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                total += ncajones*precio
                print('{nombre:>10s} {fecha:>10s} {hora:>10s} {cajones:>10s} {precio:>10s}'.format_map(record)) #  También se puede con fstring
            except:
                print(f'Fila {row[0]}: No pude interpretar: {row[1]}')
    return total


# archivo = 'ejercicios_python/Data/missing.csv'
archivo = 'ejercicios_python/Data/fecha_camion.csv'

costo = costo_camion(archivo)
print('Costo total: $', costo)
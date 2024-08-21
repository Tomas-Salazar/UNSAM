# Costo camión
import csv

def costo_camion(nombre_archivo):
    file = open(nombre_archivo, 'rt')
    rows = csv.reader(file)
    _ = next(rows)
    total = 0
    for row in rows:
        resultado = int(row[1]) * float(row[2])
        total += resultado
    file.close()
    return total


archivo = 'ejercicios_python/Data/camion.csv'
costo = costo_camion(archivo)
print('Costo total: $', costo)
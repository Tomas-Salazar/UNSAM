camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]
camion[0]            # ('Pera', 100, 490.1)
camion[2]            # ('Limon', 150, 83.44)


## Cómo armar una lista desde cero.
registros = []  # Empezamos con una lista vacía
# Usamos el .append() para agregar elementos
registros.append(('Pera', 100, 490.10))
registros.append(('Naranja', 50, 91.3))


## Un ejemplo de cómo cargar registros desde un archivo.
registros = [] # Empezamos una lista vacía
with open('ejercicios_python/Data/camion.csv', 'rt') as file:
    next(file) # Saltear el encabezado
    for line in file:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))
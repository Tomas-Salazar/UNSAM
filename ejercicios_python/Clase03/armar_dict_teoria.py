precios = {
    'Pera': 513.25,
    'Limon': 87.22,
    'Naranja': 93.37,
    'Mandarina': 44.12
}
precios['Naranja']      # 93.37
precios['Pera']         # 513.25


## Ejemplo de armado de un diccionario desde cero.
precios = {} # Empezamos con un diccionario vacío
# Agregamos elementos
precios['Pera'] = 513.25
precios['Limon'] = 87.22
precios['Naranja'] = 93.37


## Un ejemplo de cómo armar un diccionario a partir del contenido de un archivo.
precioss = {}  # Empezamos con un diccionario vacío

with open('ejercicios_python/Data/precios.csv', 'rt', encoding='utf8') as file:     # Se agrega encoding por caracteres especiales
    for line in file:
        row = line.strip().split(',')
        if row[0]:      # Ésta comprobación es para evitar cadenas vacías (False)
            precioss[row[0]] = float(row[1])
        else:
            pass
print(precioss)
# Precio Naranja

data = open('ejercicios_python/Data/precios.csv', 'rt')
for line in data:
    row = line.split(',')
    if row[0].lower() == 'naranja':
        print(f'El precio de la naranja es: ',float(row[1].strip()) )
    else:
        pass
data.close()
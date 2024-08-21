# Buscar Precios


def buscar_precio(fruta):
    data = open('ejercicios_python/Data/precios.csv', 'rt')
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


buscar_precio('frambuesa')
buscar_precio('kale')
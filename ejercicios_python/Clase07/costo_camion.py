# Ejercicios 4.4
import csv
import informe_funciones


def costo_camion(nombre_archivo):
    lista_camion = informe_funciones.leer_camion(nombre_archivo)
    total = 0
    for lote in lista_camion:
        try:
            ncajones = lote['cajones']
            precio = lote['precio']
            total += ncajones * precio
            print(f'{lote["nombre"]:>10s} {lote["cajones"]:>10d} {lote["precio"]:>10.2f}')
        except:
            print(f"No pude interpretar el lote: {lote}")
    
    return total


# archivo = 'ejercicios_python/Data/missing.csv'
archivo = 'ejercicios_python/Data/fecha_camion.csv'

costo = costo_camion(archivo)
print('Costo total: $', costo)
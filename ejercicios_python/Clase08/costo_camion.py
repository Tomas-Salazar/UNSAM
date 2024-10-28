import informe_final
import sys


def costo_camion(nombre_archivo):
    lista_camion = informe_final.leer_camion(nombre_archivo)
    total = 0
    for lote in lista_camion:
        try:
            ncajones = lote['cajones']
            precio = lote['precio']
            total += ncajones * precio
        except:
            print(f"No pude interpretar el lote: {lote}")
    
    return total


def main(params):
    nombre_archivo = params[1] if len(params) > 1 else 'ejercicios_python/Data/fecha_camion.csv'
    costo = costo_camion(nombre_archivo)
    print('Costo total:$', costo)


if __name__ == '__main__':
    main(sys.argv)
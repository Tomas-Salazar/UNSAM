import os
import sys

def archivos_png(directorio):
    '''
    Recorre todos los subdirectorios del directorio dado y devuelve una lista
    de todos los archivos con extensión .png.
    '''
    archivos = []
    for root, _, files in os.walk(directorio):  # Recorre el árbol de directorios
        for file in files:
            if file.endswith('.png'):  # Filtra archivos con extensión .png
                archivos.append(file)
    return archivos

if __name__ == '__main__':
    # Verifica que se haya pasado un directorio como argumento
    if len(sys.argv) < 2:
        print('Introducir nombre de un directorio como argumento')
        sys.exit(1)

    # Toma el directorio del primer argumento de línea de comandos
    directorio = sys.argv[1]

    # Obtiene la lista de archivos .png
    archivos = archivos_png(directorio)

    # Imprime los archivos en pantalla
    for archivo in archivos:
        print(archivo)
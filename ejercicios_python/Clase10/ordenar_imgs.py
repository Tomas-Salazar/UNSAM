# Ejercicio 10.6: Ordenar el árbol de archivos
import os
import datetime
import shutil
import sys


# Obtener y convertir la fecha del nombre del archivo
def procesar_nombre(fname):
    # Separar nombre y extensión
    nombre_base = os.path.splitext(fname)[0]  # nombre sin extensión
    ext = os.path.splitext(fname)[1]          # extensión con punto
    
    # Extraer fecha (últimos 8 caracteres antes de la extensión)
    fecha_str = nombre_base[-8:]
    fecha_datetime = datetime.datetime.strptime(fecha_str, '%Y%m%d')
    
    # Crear nuevo nombre sin fecha y guion bajo
    nuevo_nombre = nombre_base[:-9] + ext
    return nuevo_nombre, fecha_datetime


# Procesa archivo para renombrar y modificar fecha interna
def procesar(fname, fecha_datetime, ruta_origen, dir_destino):
    # Usar el directorio destino pasado como argumento
    ruta_destino = os.path.join(dir_destino, fname)
    
    # Asegurarse de que el directorio destino existe
    os.makedirs(dir_destino, exist_ok=True)
    
    # Convierte la fecha a timestamp para actualizar los metadatos
    ts_fecha = fecha_datetime.timestamp()
    
    # Verifica que el archivo origen existe
    if os.path.exists(ruta_origen):
        # Actualizar timestamps
        os.utime(ruta_origen, (ts_fecha, ts_fecha))
        # Mover archivo
        shutil.move(ruta_origen, ruta_destino)
    else:
        print(f'No se encuentra el archivo: {ruta_origen}')


def main():
    # Verificar que se proporcionaron los argumentos necesarios
    if len(sys.argv) != 3:
        print('Usar: python3 ordenar_imgs.py <directorio_origen> <directorio_destino>')
        sys.exit(1)
    
    # Obtener directorios de los argumentos y convertirlos a rutas absolutas
    dir_origen = os.path.abspath(sys.argv[1])
    dir_destino = os.path.abspath(sys.argv[2])
    
    # Verificar que existe el directorio origen
    if not os.path.exists(dir_origen):
        print(f'Error: El directorio origen "{dir_origen}" no existe')
        sys.exit(1)
    
    # Crear directorio destino si no existe
    os.makedirs(dir_destino, exist_ok=True)
    
    print(f'Procesando archivos de "{dir_origen}" a "{dir_destino}"')
    
    # Recorrer el directorio de origen
    for root, dirs, files in os.walk(dir_origen):
        for name in files:
            if name.endswith('.png'):
                ruta_archivo = os.path.join(root, name)
                nuevo_nombre, fecha_datetime = procesar_nombre(name)
                procesar(nuevo_nombre, fecha_datetime, ruta_archivo, dir_destino)
                
        for name in dirs:
            ruta_dir = os.path.join(root, name)
            # Se intenta borrar todo directorio vacío
            try:
                os.rmdir(ruta_dir)
            except Exception as e:
                print(f'No se pudo borrar el directorio: {e}')

# Para que no se ejecute el script cuando se importa el módulo
if __name__ == '__main__':
    main()
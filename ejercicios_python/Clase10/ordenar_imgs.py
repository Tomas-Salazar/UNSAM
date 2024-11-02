# Ejercicio 10.6: Ordenar el árbol de archivos
import os
import datetime
import shutil  # Para mover el archivo


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
def procesar(fname, fecha_datetime, ruta_origen):
    dir_destino = os.path.abspath(os.path.join('ejercicios_python', 'Data', 'imgs_procesadas'))
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
        print(f"No se encuentra el archivo: {ruta_origen}")


def main():
    # Crear la carpeta de destino si no existe
    dir_nuevo = os.path.join('ejercicios_python', 'Data', 'imgs_procesadas')
    if not dir_nuevo:
        os.mkdir(os.path.join('ejercicios_python', 'Data', 'imgs_procesadas'))

    # Recorrer el directorio de origen
    for root, dirs, files in os.walk("ejercicios_python/Data/ordenar"):
        for name in files:
            if name.endswith('.png'):
                ruta_archivo = os.path.join(root, name)
                nuevo_nombre, fecha_datetime = procesar_nombre(name)
                procesar(nuevo_nombre, fecha_datetime, ruta_archivo)
                
        for name in dirs:
            ruta_dir = os.path.join(root, name)
            # Se intenta borrar todo directorio vacío
            try:
                os.rmdir(ruta_dir)
            except Exception as e:
                print(f'No se pudo borrar el directorio, {e}')

# Para que no se ejecute el script cuando se importa el módulo
if __name__ == '__main__':
    main()
"""
f = open('archivo.txt', 'rt') rt es de Read Text
g = open('archivo.txt', 'wt') rt es de Write Text

data = f.read()

g.write('un texto')

f.close()
g.close()


with open(nombre_archivo, 'rt') as file:
    instrucciones


with open('foo.txt', 'rt') as file:
    data = file.read()                  # `data` es una cadena con *todo* el texto en `foo.txt`

with open(nombre_archivo, 'rt') as file:
    for line in file                    # Procesar la línea

# Para escribir cadenas:
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
"""

"""
Los ejercicios a enviar esta semana son:
El archivo buscar_precios.py del Ejercicio 2.7.
El archivo costo_camion.py del Ejercicio 2.9.
El archivo diccionario_geringoso.py del Ejercicio 2.13.
"""
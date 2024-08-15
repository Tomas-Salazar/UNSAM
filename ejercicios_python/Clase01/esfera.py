"""
Ejercicio 1.13: El volumen de una esfera
En tu directorio de trabajo de esta clase, escribí un programa llamado esfera.py que le pida a le usuarie 
que ingrese por teclado el radio r de una esfera y calcule e imprimael volumen de la misma. 
Sugerencia: recordar que el volumen de una esfera es 4/3 πr^3.

Finalmente, ejecutá el programa desde la línea de comandos para responder 
¿cuál es el volumen de una esfera de radio 6? Debería darte 904.7786842338603.
"""
import math


def volumen_esfera(r):
    volumen = (4/3) * math.pi * (r**3)
    return volumen


def main():
    while True:
        try:
            radio = float(input("Introduce el valor del radio de la esfera: "))
            
            volumen = volumen_esfera(radio)
            
            print(volumen)
            break
        
        except:
            print("Debe introducir un número válido\n")


if __name__ == '__main__':
    main()
# Ejercicio 4.7 : Formato de números
import math

value = 42863.1
print(value)

print(f'{value:0.4f}') # 4 decimales en float

print(f'{value:>16.2f}') # 16 caract, 2 decimales en float, aliniado der

print(f'{value:<16.2f}') # 16 caract, 2 decimales en float, aliniado izq

print(f'{value:*>16,.2f}') # 16 caracteres(asteriscos), 2 decimales en float, aliniado der

numero = '%.4f' %math.pi
print(numero)
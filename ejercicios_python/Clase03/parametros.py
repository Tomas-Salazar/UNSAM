# Me funciona primero yendo al directorio anterior con cd: cd C:\Users\Sala\Desktop\Python\Unsam\ejercicios_python\Clase03
# Y luego ejecutando: python parametros.py uno dos tres
import sys

param1 = int(sys.argv[1])
param2 = int(sys.argv[2])

print (param1 * param2)
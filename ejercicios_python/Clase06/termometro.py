# Ejercicio 6.6: Gaussiana
import random
import numpy as np

#La función random.normalvariate(mu,sigma) genera números aleatorios según esta distribución de probabilidades.
# Por ejemplo, usando mu = 0 y sigma = 1 podemos generar 6 valores aleatorios así:

# for i in range(6):
#     print(f'{random.normalvariate(0,1):.2f}', end=', ')
#   -0.60, 0.06, -1.33, -0.62, -0.81, 0.63, 

def medir_temp(n):
    mu = 0
    sigma = 0.2
    temp_real = 37.5
    
    mediciones = [temp_real + random.normalvariate(mu, sigma) for _ in range(n)]
    np.save('ejercicios_python/Data/temperaturas.npy', mediciones)
    return mediciones

def resumen_temp(n):
    mediciones = medir_temp(n)
    mediciones.sort()
    cantidad_mediciones = len(mediciones)
    
    valor_max = round(max(mediciones), 2)
    valor_min = round(min(mediciones), 2)
    promedio = round(sum(mediciones) / cantidad_mediciones, 2)
    
    if cantidad_mediciones % 2 != 0:
        indice_mediana = (cantidad_mediciones-1) // 2
        mediana = mediciones[indice_mediana]
    else:
        indice_mediana = (cantidad_mediciones) // 2
        mediana1, mediana2 = mediciones[indice_mediana]-1, mediciones[indice_mediana]
        mediana = (mediana1 + mediana2) / 2
    
    return (valor_max, valor_min, promedio, round(mediana,2))

n = 999
evaluacion = resumen_temp(n)
print(evaluacion)
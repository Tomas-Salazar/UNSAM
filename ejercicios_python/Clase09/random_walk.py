import matplotlib.pyplot as plt
import numpy as np

# Ejercicio 9.2: Caminatas al azar
N = 10000
colores = ['b', 'g', 'r', 'c', 'm', 'y', 'k','orange','purple','brown','pink','gray']

def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)    
    return pasos.cumsum()

# Crea la figura 
fig = plt.figure(figsize=(10, 8))

# Subplot superior (más grande)
plt.subplot(2, 1, 1)
plt.title('12 Caminatas al azar')
plt.xlabel('tiempo')
plt.ylabel('distancia al origen')

max_distancia = 0  # Para encontrar la que más se aleja
min_distancia = float('inf')  # Para asegurarnos de encontrar el menor valor

# Generar y guardar todas las caminatas
for i in range(12):
    caminata = randomwalk(N)
    plt.plot(caminata, color=colores[i])
    
    # Encontrar la máxima distancia alcanzada (en valor absoluto)
    distancia_maxima = np.max(np.abs(caminata))
    
    if distancia_maxima > max_distancia:
        max_distancia = distancia_maxima
        caminata_mas_lejana = caminata
    if distancia_maxima < min_distancia:
        min_distancia = distancia_maxima
        caminata_mas_cercana = caminata

# Subplot inferior izquierdo (caminata más lejana)
plt.subplot(2, 2, 3)
plt.title('La caminata que más se aleja')
plt.xlabel('tiempo')
plt.ylabel('distancia al origen')
plt.plot(caminata_mas_lejana, 'r')

# Subplot inferior derecho (caminata más cercana)
plt.subplot(2, 2, 4)
plt.title('La caminata que menos se aleja')
plt.xlabel('tiempo')
plt.ylabel('distancia al origen')
plt.plot(caminata_mas_cercana, 'g')

plt.show()
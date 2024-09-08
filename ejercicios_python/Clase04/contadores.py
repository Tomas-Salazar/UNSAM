"""
Ejercicio 4.6: Contadores
Vamos a usar un contador (objeto Counter) para contar cajones de frutas. Probalo:
"""
from collections import Counter
from informe import leer_camion

camion = leer_camion('ejercicios_python/Data/camion.csv')
tenencias = Counter()
for i in camion:
    tenencias[i['nombre']] += i['cajones']  # Busca por nombre y suma cajones
    tenencias
Counter({'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150}) #print
# la entradas múltiples como Mandarina y Naranja en camion se combinan en una sola entrada

# Podés listar las tres frutas con mayores tenencias:
most_common = tenencias.most_common(3)
print('Print most_common:\n',most_common)
[('Mandarina', 250), ('Naranja', 150), ('Caqui', 150)] #print


# Carguemos los datos de otro camión con cajones de fruta en un nuevo contador:
camion2 = leer_camion('ejercicios_python/Data/camion2.csv')
tenencias2 = Counter()
for i in camion2:
    tenencias2[i['nombre']] += i['cajones']
tenencias2
Counter({'Durazno': 125, 'Frambuesa': 250, 'Lima': 50, 'Mandarina': 25}) #print
print('Print camion2:\n',tenencias2)

# Y finalmente combinemos las tenencias de ambos camiones con una operación simple:
tenencias
Counter({'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150}) #print
tenencias2
Counter({'Frambuesa': 250, 'Durazno': 125, 'Lima': 50, 'Mandarina': 25}) #print
combinada = tenencias + tenencias2
combinada
Counter({'Caqui': 150, 'Durazno': 220, 'Frambuesa': 250, 'Lima': 150, 'Mandarina': 275, 'Naranja': 150}) #print
print('Print combinada:\n',combinada)
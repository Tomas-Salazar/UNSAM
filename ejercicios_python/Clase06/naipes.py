import random


def obtener_cartas():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['Oro', 'Copa', 'Espada', 'Basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    
    mano = [] # La función se resume a:    mano = random.sample(naipes,k=3)
    while len(mano) < 3:
        carta = random.choice(naipes)
        mano.append(carta)
        naipes.remove(carta)
    return mano


# mano = obtener_cartas()
# print(mano)

# Con random.choice(naipes) podemos elegir 3 valores, usando k como parámetro:
# random.choices(naipes, k=3) pero pueden repetirse.

# Para eso utilizamos: random.sample(naipes,k=3) que toma una muestra de 3 valores únicos.



valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
print(naipes)
random.shuffle(naipes) # Suffle mezcla
print(naipes)
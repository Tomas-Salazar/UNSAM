# Ejercicio 6.1: Generala servida
import random
from collections import Counter


def tirar():
    lista = []
    for _ in range(5):
        lista.append(random.randint(1,6))
    return lista


def es_generala(tirada):
    if tirada[0] == tirada[1] == tirada[2] == tirada[3] == tirada[4]:
        return True
    else:
        return False


# def calcular_una_generala():
#     cantidad_tiros = 0
#     generala = False

#     while not generala:
#         cantidad_tiros += 1
#         tiros = tirar()
#         # print(tiros)
#         generala = es_generala(tiros)
#         prob = 1 / cantidad_tiros
#     print(f'\nTiros necesarios para lograr generala: {cantidad_tiros}.')
#     print(f'Podemos estimar la probabilidad de sacar generala servida en {prob:.6}%.\n')


# def calcular_n_tiros_generalas(N):
#     G = sum([es_generala(tirar()) for _ in range(N)])
#     prob = G/N
#     print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
#     print(f'Podemos estimar la probabilidad de sacar generala servida en {prob:.6f}%.')
#     return prob


# n_tiros = 1000000
# # calcular_una_generala()       # Se que se pueden unificar pero ya la había hecho antes
# calcular_n_tiros_generalas(n_tiros)



# Ejercicio 6.2: Generala no necesariamente servida

def prob_generala(N):
    G = 0
    for _ in range(N):
        tirada = tirar()
        counter = Counter(tirada)
        valor_mas_comun, _ = counter.most_common(1)[0]
        
        tirada = [dado if dado == valor_mas_comun else random.randint(1, 6) for dado in tirada]
        tirada = [dado if dado == valor_mas_comun else random.randint(1, 6) for dado in tirada]
        
        if es_generala(tirada):
            G += 1
        else:
            pass
    return G/N


N = 1000
print(prob_generala(N))
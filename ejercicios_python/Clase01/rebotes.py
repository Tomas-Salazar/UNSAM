# Rebotes

altura = 100
rebotes = 10
indice_perdida = 3/5

# def calcular_rebotes(altura, rebotes, indice):
#     i = 0
#     for _ in range(rebotes):
#         i += 1
#         altura *= indice
#         print(f'Rebote número: {i}')
#         print(f'Altura alcanzada: {round(altura, 4)} metros')
#         print('')

# calcular_rebotes(altura, rebotes, indice_perdida)

for _ in range(rebotes):
    altura *= indice_perdida
    print(f'{round(altura, 4)}')
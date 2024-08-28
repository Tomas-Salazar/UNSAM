import sys

if len(sys.argv) > 1:
    param1 = int(sys.argv[1])
else:
    param1 = 100

altura = param1
rebotes = 10
indice_perdida = 3/5

for _ in range(rebotes):
    altura *= indice_perdida
    print(f'{round(altura, 4)}')
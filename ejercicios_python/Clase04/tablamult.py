# Ejercicio 4.12: Tablas de multiplicar

header = ''.join([f'{i:4d}' for i in range(10)])
division = '-' * 45
print(f'   {header}')
print(f'{division}')

for i in range(10):
    fila = [0] * 10
    for j in range(1, 10):
        fila[j] = fila[j-1] + i
    
    print(f' {i}:', end='') # El end es para no usar el \n que me rompería el resto de la línea
    for num in fila:
        print(f'{num:4d}', end='')
    print()
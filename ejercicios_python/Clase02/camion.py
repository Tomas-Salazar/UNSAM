# Camión

# import os

# print(os.getcwd())

# with open('ejercicios_python/Data/camion.csv', 'rt') as file:
#         for line in file:
#             print(line, end='')

# data = open('ejercicios_python/Data/camion.csv', 'rt')
# headers = next(data)
# for line in data:
#     print(line, end="")
# data.close()

data = open('ejercicios_python/Data/camion.csv', 'rt')
headers = next(data).split(',')
for line in data:
    row = line.split(',')
    print(row)
data.close()
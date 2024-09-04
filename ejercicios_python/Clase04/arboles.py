import csv
from pprint import pprint

with open('ejercicios_python/Data/arbolado-en-espacios-verdes.csv', 'rt', encoding='utf8') as file:
    rows = csv.reader(file)
    headers = next(rows)
    print(headers)
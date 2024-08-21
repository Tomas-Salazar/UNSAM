import gzip

with gzip.open('ejercicios_python/Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')
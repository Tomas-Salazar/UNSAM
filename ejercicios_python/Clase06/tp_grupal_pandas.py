import csv
from collections import defaultdict

data_divorcios = 'ejercicios_python/data/dataset_divorcios.csv'
# data_matrimonios = 'ejercicios_python/data/matrimonios_2018.csv'

def catalogar(nombre_archivo):
    with open(nombre_archivo, encoding="utf8") as f:
        rows=csv.reader(f)
        encabezado=next(rows)
        catalogo = defaultdict(int)
        for row in rows:
        
            # Año de casamiento y el año de divorcio
            fecha_casamiento = row[3]
            fecha_divorcio = row[0]
            
            # Paso a años
            año_casamiento = fecha_casamiento[5:9]
            año_divorcio = fecha_divorcio[5:9]
            
            # Clave como tupla
            clave = (row[1], row[2], año_casamiento, año_divorcio)
            
            # Incrementar el contador en el diccionario
            catalogo[clave] += 1
        
    return dict(catalogo)

catalogo = catalogar(data_divorcios)
# print(catalogo)


def analizar_cat(path):
    with open(path, 'rt', encoding='utf8') as file:
        rows = csv.reader(file)
        headers = next(rows)
        row = next(rows)
        lista =[]
        lista2 =[]
        for row in rows:
            row[0] = row[0][5:9]
            row[3] = row[3][5:9]
            lista.append(row)
        print(min(lista))
        for row in lista:
            t1 = int(row[3])
            t2 = int(row[0])
            if t1 <= t2 and t1 >= 1900 and t2 <= 2024:
                t3 = t2-t1
                lista2.append(t3)
            else:
                print(row)
    return lista2

data1 = analizar_cat(data_divorcios)
promedio_casamientos = sum(data1)/len(data1)
print('Los años promedio de casamientos son de: ',round(promedio_casamientos, 2))
casamiento_max = min(data1)
casamiento_min = max(data1)
print(f'El casamiento de mayor duración fue de: {casamiento_max} años')
print(f'El casamiento de menor duración fue de: {casamiento_min} años')
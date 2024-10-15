import csv

data_divorcios = 'ejercicios_python/data/dataset_divorcios.csv'
data_matrimonios = 'ejercicios_python/data/matrimonios_2018.csv'


def normalizar_fecha(valor_fecha):
    dia = valor_fecha[0:2]
    mes_str = valor_fecha[2:5]
    anio = valor_fecha[5:9]

    meses = {
        "JAN": "01", "FEB": "02", "MAR": "03", "APR": "04",
        "MAY": "05", "JUN": "06", "JUL": "07", "AUG": "08",
        "SEP": "09", "OCT": "10", "NOV": "11", "DEC": "12"
    }
    mes = meses[mes_str.upper()]
    fecha_normalizada = f"{anio}-{mes}-{dia}"
    
    return fecha_normalizada


def catalogar(archivo):
    dict_catalogo = {}
    with open(archivo, 'rt', encoding='utf-8') as file:
        rows = csv.reader(file)
        headers = next(rows)
        headers[0] = 'Fecha_divorcio'
        headers[1] = 'Genero_1'
        headers[2] = 'Genero_2'
        headers[3] = 'Fecha_matrimonio'
        
        for i, row in enumerate(rows, start=1):
            try:
                dict_cat = dict(zip(headers, row))
                dict_cat['Fecha_divorcio'] = normalizar_fecha(dict_cat['Fecha_divorcio'])
                dict_cat['Fecha_matrimonio'] = normalizar_fecha(dict_cat['Fecha_matrimonio'])
                
                anio_matrimonio = dict_cat['Fecha_matrimonio'][:4]
                anio_divorcio = dict_cat['Fecha_divorcio'][:4]
                
                clave = (dict_cat['Genero_1'], dict_cat['Genero_2'], anio_matrimonio, anio_divorcio)
                
                if clave in dict_catalogo:
                    dict_catalogo[clave] += 1
                else:
                    dict_catalogo[clave] = 1
                
            except ValueError:
                    print('Faltan datos en la línea', i, 'del archivo.')
    return dict_catalogo

df_divorcios = catalogar(data_divorcios)
print(df_divorcios)
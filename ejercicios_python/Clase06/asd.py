from datetime import date, timedelta, datetime
import datetime

# Ejercicio 6.3: Cocumpleaños

def obtener_dias_del_ano(anio):
    # Definir el primer día del año
    primer_dia = date(anio, 1, 1)
    # Definir el primer día del siguiente año
    ultimo_dia = date(anio + 1, 1, 1)
    
    # Iterar sobre cada día hasta el último día del año
    dias_del_ano = []
    dia_actual = primer_dia
    while dia_actual < ultimo_dia:
        dias_del_ano.append(dia_actual)
        dia_actual += timedelta(days=1)
    
    return dias_del_ano

# Ejemplo: obtener los días del año 2024
dias_2024 = obtener_dias_del_ano(2024)
dias_2024_str = [datetime.date.strftime(dia, '%d-%m-%Y') for dia in dias_2024]

# Mostrar los primeros 10 días del año
print(dias_2024_str[:10])

"""
Haga lo siguiente: numere los días del año del 1 al 365 (suponiendo que no es un año bisiesto). 
Por ejemplo, el número 1 es el 1 de enero y el 365 el 31 de diciembre. Dígale al programa que elija 30 números entre esos 365 
en forma aleatoria. Este dato es vital: tienen que ser elegidos al azar. 
Elige un número y lo repone a los 365 que tenía originalmente. 
De esta forma, entre los 30 números puede aparecer alguno repetido. 
Cuando haya terminado el proceso y ya tiene estos 30 números fíjese -justamente- si hay al menos algún par repetido, 
que corresponderían al mismo día del año. Repita el proceso 10 mil veces (por supuesto, con la ayuda de una computadora). 
Fíjese en cuántos de los 10 mil casos de muestra aparecen números repetidos. Divida ese número por 10 mil. 
Verá que el número que obtiene es (aproximadamente) 0.7129… 
¿Cómo se interpreta esto? Esto significa que con 30 personas en una habitación, las chances de que haya dos 
que cumplan años el mismo día ¡supera el 71 por ciento! 
"""
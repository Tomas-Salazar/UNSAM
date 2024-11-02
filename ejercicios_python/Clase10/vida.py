import datetime

# Ejercicio 10.1: Segundos vividos
def vida_en_segundos(fecha):
    # Se asume que se nace a las 00:00 hs y el formato de entrada de la fecha es 'dd/mm/AAAA'
    fecha_nacimiento = datetime.datetime.strptime(fecha, '%d/%m/%Y')
    fecha_hoy = datetime.datetime.now()
    diferencia = fecha_hoy - fecha_nacimiento  # Diferencia entre las fechas
    segundos_totales = diferencia.total_seconds()
    return segundos_totales

fecha_tom = vida_en_segundos('04/11/1998')
print(round(fecha_tom))
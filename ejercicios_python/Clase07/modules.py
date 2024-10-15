import rebotes
import hipoteca
import informe_funciones
from fileparse import parse_csv


camion = parse_csv('ejercicios_python/Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
print(camion)

lista_precios = parse_csv('ejercicios_python/Data/precios.csv', types = [str, float], has_headers = False)
print(lista_precios)

precios = dict(lista_precios)
print(precios)
print(precios['Naranja'])
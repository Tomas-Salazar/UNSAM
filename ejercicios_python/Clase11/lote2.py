import fileparse
from pprint import pprint

with open('ejercicios_python/Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def mostrar_info(self):
        print('Nombre de fruta: ', self.nombre)
        print('Numero de cajones: ', self.cajones)
        print('Precio por cajon: ', self.precio)
    
    def vender(self, n_vendidos):
        self.n_vendidos = n_vendidos
        self.cajones -= n_vendidos
        
    def calcular_costo(self):
        self.costo = self.precio * self.cajones
        
        return self.costo


camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
print(camion)

sumatoria = sum([c.calcular_costo() for c in camion])
print(sumatoria)
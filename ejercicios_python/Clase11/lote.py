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
        
        print(self.costo)


lote = Lote('Pera', 100, 490.10)
lote.calcular_costo()

lote.vender(50)
print(lote.cajones)
lote.calcular_costo()
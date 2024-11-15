# canguros_buenos
class Canguro:
    def __init__(self, nombre, lista=None):
        self.nombre = nombre
        self.lista = lista if lista is not None else []
        
        self.contenido_marsupio = []
    
    def meter_en_marsupio(self, item=None):
        if item is not None:    # Item individual
            self.contenido_marsupio.append(item)
        elif self.lista:        # Lista del inicio
            self.contenido_marsupio.extend(self.lista)
        else:
            print('No hay nada para añadir al marsupio.')
    
    def __str__(self):
        return f'Nombre = {self.nombre}, Contenido marsupio = {self.contenido_marsupio}'


cangurito = Canguro('Bebé Canguro')
lista_marsupio = [cangurito.nombre, 'hojas', 'tierra', 'cordón umbilical']
madre_canguro = Canguro('Madre Canguro', lista_marsupio)
madre_canguro.meter_en_marsupio()

print(madre_canguro)
print(madre_canguro.contenido_marsupio)
print(cangurito)





# canguro_malo.py

"""Este código continene un 
bug importante y dificil de ver
"""

# class Canguro:
#     """Un Canguro es un marsupial."""
    
#     def __init__(self, nombre, contenido=[]):
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         self.contenido_marsupio = contenido

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)

# #%%
# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)

# print(cangurito.contenido_marsupio)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.


"""
El problema del código de canguro malo, es que todas las instancias de Canguro que no 
especifiquen un contenido compartirán la misma lista.

"""
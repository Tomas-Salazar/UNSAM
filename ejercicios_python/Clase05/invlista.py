# Ejercicio 5.5: Invertir una lista

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0, e)
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))



def invertir_lista2(lista):
    invertida = lista[::-1]
    return invertida

print(invertir_lista2([1, 2, 3, 4, 5]))
print(invertir_lista2(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
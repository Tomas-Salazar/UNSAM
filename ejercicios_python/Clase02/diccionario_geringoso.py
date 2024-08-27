"""
Ejercicio 2.13: Diccionario geringoso.
Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. 
Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones 
al geringoso (como en el Ejercicio 1.18). 
Probá tu función para la lista ['banana', 'manzana', 'mandarina']. 
Guardá este ejercicio en un archivo diccionario_geringoso.py para entregar al final de la clase.
"""
frutas = ['banana', 'manzana', 'mandarina']


def geringoso(lista):
    nueva_lista = []
    for palabra in lista:
        cadena = ''
        for letra in palabra:
            if letra.lower() == 'a' or letra.lower() == 'á':
                    cadena += letra + 'pa'
                    
            elif letra.lower() == 'e' or letra.lower() == 'é':
                    cadena += letra + 'pe'
                    
            elif letra.lower() == 'i' or letra.lower() == 'í':
                    cadena += letra + 'pi'
                    
            elif letra.lower() == 'o' or letra.lower() == 'ó':
                    cadena += letra + 'po'
                    
            elif letra.lower() == 'u' or letra.lower() == 'ú':
                    cadena += letra + 'pu'
            else:
                    cadena += letra
        nueva_lista.append((palabra, cadena))
    diccionario_geningoso = dict(nueva_lista)
    return diccionario_geningoso


print(geringoso(frutas))
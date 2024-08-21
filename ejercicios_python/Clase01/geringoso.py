"""
Ejercicio 1.18: Geringoso rústico
Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' 
según corresponda luego de cada vocal.

cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
        ?
capadepenapa
Geperipingoposopo

Podés probar tu código cambiando la cadena inicial por otra palabra, como 'apa' o 'boligoma'.
Guardá el código en un archivo geringoso.py.
"""
def geringoso(cadena):
        palabra = ''
        for letra in cadena:
                if letra.lower() == 'a' or letra.lower() == 'á':
                        palabra += letra + 'pa'
                        
                elif letra.lower() == 'e' or letra.lower() == 'é':
                        palabra += letra + 'pe'
                        
                elif letra.lower() == 'i' or letra.lower() == 'í':
                        palabra += letra + 'pi'
                        
                elif letra.lower() == 'o' or letra.lower() == 'ó':
                        palabra += letra + 'po'
                        
                elif letra.lower() == 'u' or letra.lower() == 'ú':
                        palabra += letra + 'pu'
                        
                else:
                        palabra += letra
        return palabra


def main():
        palabra_elegida = input('Indique su texto a traducir en gangoso: ')
        palabra_geringosa = geringoso(palabra_elegida)
        print(palabra_geringosa)


if __name__ == '__main__':
        main()
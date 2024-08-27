#Un conjunto es una colección de elementos únicos sin orden y sin repetición.

citricos1 = { 'Naranja','Limon','Mandarina' }
# Alternativamente podemos escribirlo así:
citricos1 = set(['Naranja', 'Limon', 'Mandarina'])


# Los conjuntos son útiles para evaluar pertenencia.
citricos2 = { 'Naranja','Limon','Mandarina' }
set(['Naranja', 'Limon', 'Mandarina'])
'Naranja' in citricos2   # True
'Manzana' in citricos2   # False


# Los conjuntos también son útiles para eliminar duplicados.
nombres = ['Naranja', 'Manzana', 'Pera', 'Naranja', 'Pera', 'Banana']
unicos = set(nombres)      # {'Manzana', 'Banana', 'Naranja', 'Pera'}


# Más operaciones en conjuntos:
citricos3 = { 'Naranja','Limon','Mandarina' }
citricos3.add('Banana')      # Agregar un elemento
citricos3.remove('Limon')    # Eliminar un elemento

#   A | B                 # Unión de conjuntos A y B
#   A & B                 # Intersección de conjuntos
#   A - B                 # Diferencia de conjuntos
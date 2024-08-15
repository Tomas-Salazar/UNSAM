# Ejercicio 1.12: Un misterio
# ¿podrías explicar el siguiente comportamiento?

# >>> bool("False")
# True
# >>>

# Lo que sucede es que se evalúa si esa cadena existe o no está vacía, y en verdad, existe, por eso da true
print(bool("False"))
print(bool("True"))

# Diferente es si la cadena estuviese vacía, o se evaluara el valor False como booleano y no como string
print(bool(""))
print(bool(False))

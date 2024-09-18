# Ejercicio 6.5: Calcular pi
# La funcion random.random() genera un número de punto flotante entre 0 y 1.
import random


def generar_punto(cantidad_puntos=1):
    puntos = [(random.random(),random.random()) for _ in range(cantidad_puntos)]
    return puntos


# Función para estimar pi
def estimar_pi(cantidad_puntos=100000):
    puntos = generar_punto(cantidad_puntos)
    dentro_del_circulo = 0

    # Contamos cuántos puntos están dentro del círculo
    for x, y in puntos:
        if x**2 + y**2 < 1:  # Verificamos si el punto está dentro del círculo
            dentro_del_circulo += 1

    # Proporción de puntos dentro del círculo
    proporcion = dentro_del_circulo / cantidad_puntos

    # Estimación de pi usando la fórmula pi ≈ 4 * proporción
    pi_estimado = 4 * proporcion
    return pi_estimado

pi_aproximado = estimar_pi()
print(f"El valor aproximado de pi es: {pi_aproximado}")

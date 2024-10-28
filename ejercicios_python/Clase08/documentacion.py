def valor_absoluto(n):
    """Calcula el valor absoluto de un número, donde n debe ser un número real.
    Devuelve el valor absoluto de n
    
    Parámetros:
        n: Un número real
    Devuelve:
        El valor absoluto de n
    """
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    """Calcula la suma de los números pares en una lista.
    l debe ser una lista de números enteros y devuelve la suma de los números pares en l
    
    Parámetros:
        l: Una lista de números enteros
    Devuelve:
        La suma de todos los números pares en la lista
    """
    res = 0  # Acumulador
    for e in l:
        if e % 2 == 0:  # Verifica resto 0
            res += e
            
    return res
# Invariante del ciclo: res


def veces(a, b):
    """Multiplica dos números mediante sumas sucesivas.
    a debe ser un número real, b debe ser un entero no negativo
    Devuelve el producto de a * b
    """
    res = 0      # Acumulador del resultado
    nb = b       # Contador de iteraciones restantes
    while nb != 0:
        res += a  # Suma 'a' tantas veces como indique 'b'
        nb -= 1   # Resta una iteración
    return res
# Invariante del ciclo: En cada iteración, res = a * (b - nb) donde nb es el número de iteraciones que faltan


def collatz(n):
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
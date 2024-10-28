import sys


def rebotar(altura, rebotes, indice_perdida=3/5):
    for i in range(1, rebotes + 1):
        altura *= indice_perdida
        print(f'{i}:  {round(altura, 2)}')


def main():
        # Lee los parámetros desde la línea de comandos si es que hay
        if len(sys.argv) > 1:
            param1 = int(sys.argv[1])
            rebotes = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        else:
            param1 = 100
            rebotes = 10
        
        # Llama a la función rebotar con los parámetros obtenidos
        rebotar(param1, rebotes)


if __name__ == "__main__":
    main()
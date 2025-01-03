class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


class TorreDeControl:
    '''Representa una torre de control de un aeropuerto con una pista.
    Los aviones que esperan para aterrizar tienen prioridad sobre los que
    esperan para despegar.'''
    
    def __init__(self):
        self.arribos = Cola()       # Se crea el objeto cola de arribos
        self.partidas = Cola()      # Se crea el objeto cola de partidas
    
    def nuevo_arribo(self, vuelo):
        self.arribos.encolar(vuelo)     # Agrega vuelo a la cola de arribos
    
    def nueva_partida(self, vuelo):
        self.partidas.encolar(vuelo)    # Agrega vuelo a la cola de partidas
    
    def ver_estado(self):
        '''Muestra el estado actual de las colas'''
        arribos = ', '.join(self.arribos.items)
        partidas = ', '.join(self.partidas.items)
        print(f'Vuelos esperando para aterrizar: {arribos}')
        print(f'Vuelos esperando para despegar: {partidas}')
    
    def asignar_pista(self):
        '''Asigna la pista a un vuelo, dando prioridad a los arribos'''
        if not self.arribos.esta_vacia():
            vuelo = self.arribos.desencolar()
            print(f'El vuelo {vuelo} aterrizó con éxito.')
        elif not self.partidas.esta_vacia():
            vuelo = self.partidas.desencolar()
            print(f'El vuelo {vuelo} despegó con éxito.')
        else:
            print('No hay vuelos en espera.')


# torre = TorreDeControl()
# torre.nuevo_arribo('AR156')
# torre.nueva_partida('KLM1267')
# torre.nuevo_arribo('AR32')
# torre.ver_estado()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
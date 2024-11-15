class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)


class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __str__(self):
        return f'Rectangulo({self.p1}, {self.p2})'
    
    def __repr__(self):
        return f'Rectangulo({repr(self.p1)}, {repr(self.p2)})'
    
    def base(self):
        return abs(self.p2.x - self.p1.x)
    
    def altura(self):
        return abs(self.p2.y - self.p1.y)
    
    def area(self):
        return self.base() * self.altura()
    
    def desplazar(self, desplazamiento):
        self.p1 = self.p1 + desplazamiento
        self.p2 = self.p2 + desplazamiento
    
    def rotar(self):
        # Rota el rectángulo 90 grados a la derecha sobre su esquina inferior derecha
        
        x_max = max(self.p1.x, self.p2.x)
        y_min = min(self.p1.y, self.p2.y)
        punto_rotacion = Punto(x_max, y_min) # Identificamos esquina inf izq
        
        base_anterior = self.base()          # Identificamos base
        altura_anterior = self.altura()      # Identificamos altura
        # Armamos rectangulo
        if self.p1.x <= self.p2.x and self.p1.y >= self.p2.y:
            self.p1 = Punto(punto_rotacion.x - altura_anterior, punto_rotacion.y)
            self.p2 = Punto(punto_rotacion.x, punto_rotacion.y + base_anterior)
        elif self.p1.x >= self.p2.x and self.p1.y >= self.p2.y:
            self.p1 = punto_rotacion
            self.p2 = Punto(punto_rotacion.x - altura_anterior, punto_rotacion.y + base_anterior)
        elif self.p1.x <= self.p2.x and self.p1.y <= self.p2.y:
            self.p1 = Punto(punto_rotacion.x - altura_anterior, punto_rotacion.y)
            self.p2 = Punto(punto_rotacion.x, punto_rotacion.y + base_anterior)
        else:
            self.p1 = punto_rotacion
            self.p2 = Punto(punto_rotacion.x - altura_anterior, punto_rotacion.y + base_anterior)
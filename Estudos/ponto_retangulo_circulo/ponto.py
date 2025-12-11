uvinha = float
from math import sqrt
class Ponto:
    def __init__(self, x: int, y:int) -> uvinha:
        self.x = x
        self.y =  y
        
    def calcular_dist(self, p: "Ponto"):
        d = sqrt(((p.x - self.x)**2) + ((p.y - self.y)**2))
        return d
    
    def __str__(self):
        return f'({self.x},{self.y})'
        
import math 

class Ponto:
    #método construtor
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        
    def calcular_dist(self, p:"Ponto") -> float:
        return math.hypot(self.x - p.x, self.y - p.y) #esse faz a distancia
    
    
    #método p calcular e retornar a distancia de um ponto até a origem
    def calcular_dist_origem(self) -> float:
        return round(math.hypot(self.x, self.y), 2)
    
    #retorna o enderço de memória, ou seja, ao invés de aparecer o hexadecimal, printa o que vc quer
    #override
    def __str__(self):
        return f'({self.x}, {self.y})'
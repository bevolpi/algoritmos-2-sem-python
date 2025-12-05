# 02_coordenadas
from ponto import Ponto

class Retangulo:
    def __init__(self, canto_sup_esq: Ponto, largura = 0, altura = 0):
        self.canto_sup_esq = canto_sup_esq #atributo do objeto -> "(x, y)" ---> self.canto_sup_esq.x = pega o valor do x dentro do atributo 
        self.largura = largura # atributo do objeto -> "l"
        self.altura = altura # atributo do objeto -> "h"
    
    # método para calcular e retornar o perímetro 
    def calcular_area(self):
        return self.altura * self.largura
    
    # método para calcular e retornar o perímetro            
    def calcular_perimetro(self):
        return round(2 * (self.altura + self.largura), 2)
    
    # método para aumentar o tamanho do retangulo
    def aumentar_tamanho(self, altura: float, largura: float) -> float:
        self.largura += largura
        self.altura += altura
    
    # método para retornar a coordenada do centro do retangulo
    def coordenada_centro(self) -> Ponto:
        xc = round((self.canto_sup_esq.x + self.largura / 2), 2) # é a metade da largura - o ponto -> p dar o x do centro
        yc = round((self.canto_sup_esq.y - self.altura / 2), 2)
        return Ponto(xc, yc)
        
        
    def __str__(self) -> str:
        return f'Área = {self.calcular_area():<10} | Perímetro = {self.calcular_perimetro():<10} | Centro = {self.coordenada_centro()}'


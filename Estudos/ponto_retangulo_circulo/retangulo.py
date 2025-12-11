from ponto import Ponto
class Retangulo:
    
    def __init__(self, altura, largura, canto_se:Ponto):
        self.altura = altura
        self.largura = largura
        self.canto_se = canto_se
        
    def calcular_area(self):
        return self.altura*self.largura

    def calcular_perimetro(self):
        return self.altura * 2 + self.largura * 2
    
    def aumentar_retangulo(self, alt_aum: int, lar_aum:int):
        altura = self.altura + alt_aum
        largura = self.largura + lar_aum
        return Retangulo(altura, largura, self.canto_se)
    
    def centro(self):
        x_centro = self.largura - self.canto_se.x
        y_centro = self.altura - self.canto_se.y
        return Ponto(x_centro, y_centro)
    
    def __str__(self):
        return f'Área = {self.calcular_area():<10} | Perímetro = {self.calcular_perimetro():<10} | Centro = {self.centro()}'
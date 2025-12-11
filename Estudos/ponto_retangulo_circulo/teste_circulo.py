'''Escreva uma classe em python denominada Circulo, com os atributos centro e
raio, onde centro é um objeto Ponto e raio é um número.
Instancie um objeto Circulo, que represente um círculo. Escreva uma função
denominada ponto_no_circulo, que receba um Circulo e um Ponto e retorne True,
se o ponto estiver dentro ou no limite do círculo.
Escreva uma função chamada retangulo_no_circulo, que receba como parâmetro
um Circulo e um Retangulo e retorne True, se o retângulo estiver totalmente
dentro ou no limite do círculo.'''
from ponto import Ponto
from circulo import Circulo
from retangulo import Retangulo

def ponto_no_circulo(c:Circulo, p:Ponto):
    d = c.centro.calcular_dist(p)
    if d  > c.raio:
        return False
    return True
    
def retangulo_no_circulo(c:Circulo, r:Retangulo):
    
    # Coordenadas do Canto Superior Esquerdo (SE)
    x_se = r.canto_se.x
    y_se = r.canto_se.y
    
    # Canto Superior Esquerdo (SE) - Ponto(x, y)
    p_se = r.canto_se
    # Canto Superior Direito (SD) - Ponto(x + largura, y)
    p_sd = Ponto(x_se + r.largura, y_se)
    # Canto Inferior Esquerdo (IE) - Ponto(x, y - altura)
    p_ie = Ponto(x_se, y_se - r.altura)
    # Canto Inferior Direito (ID) - Ponto(x + largura, y - altura)
    p_id = Ponto(x_se + r.largura, y_se - r.altura)
    # 2. Verificando se TODOS os 4 cantos estão no círculo
    # O retângulo só está DENTRO se todos os cantos estiverem.
    return (ponto_no_circulo(c, p_se) and
            ponto_no_circulo(c, p_sd) and
            ponto_no_circulo(c, p_ie) and
            ponto_no_circulo(c, p_id))

def main():
    centro = Ponto(3,2)
    raio = 2
    
    print("Ponto q quero achar: ")
    p  = Ponto(int(input("X =")), int(input('Y=')))
    
    res_ponto = ponto_no_circulo(Circulo(centro, raio), p)
    
    res_retangulo = retangulo_no_circulo
    
    if res_ponto:
        print("Ponto no círculo!!")
    else:
        print("Ponto fora!")
        
    if res_retangulo:
        print("Retangulo no círculo!!")
    else:
        print("Rteangulo fora!")
    
    
if __name__ == '__main__':
    main()
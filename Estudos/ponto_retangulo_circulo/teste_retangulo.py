'''Codifique um Tipo Abstrato de Dados (TAD) no python chamado Retangulo. O tipo
criado deverá ter como atributos a largura, a altura e a coordenada do canto
superior esquerdo (utilizar a classe Ponto criada no exercício anterior). O
construtor deverá ser codificado.
 Implemente um método para calcular e retornar a área do retângulo.
 Implemente um método para calcular e retornar o perímetro de um retângulo.
 Implemente um método para aumentar o tamanho do retângulo
 Implemente uma função que calcule e retorne a coordenada do centro de um
retângulo.
 Crie uma lista de retângulos e imprima no console:
 A coordenada do centro de cada retângulo, o valor da área e do perímetro'''


from retangulo import Retangulo
from ponto import Ponto

def main():
    altura = float(input('altura:'))
    largura = float(input('largura:'))
    canto_se = Ponto(int(input('X=')), int(input('Y=')))
    
    r = Retangulo(altura, largura, canto_se)
    
    # area = r.calcular_area()
    # perimetro = r.calcular_perimetro()
    
    # mesmo que não imprima, está aqui caso precise
    altura_aum = float(input("Quanto quer aumentar na altura? "))
    largura_aum = float(input("Quanto quer aumentar na largura? "))
    
    # r_atualizado = r.aumentar_retangulo(altura_aum, largura_aum)
    # centro = r.centro()
    
    print(r)
    
if __name__ == '__main__':
    main()
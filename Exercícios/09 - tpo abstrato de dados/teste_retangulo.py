'''Codifique um Tipo Abstrato de Dados (TAD) no python chamado Retangulo. O tipo  criado deverá ter como atributos a largura, a altura e a coordenada do canto superior esquerdo (utilizar a classe Ponto criada no exercício anterior). O construtor deverá ser codificado.
 Implemente um método para calcular e retornar a área do retângulo.
 Implemente um método para calcular e retornar o perímetro de um retângulo.
 Implemente um método para aumentar o tamanho do retângulo
 Implemente uma função que calcule e retorne a coordenada do centro de um retângulo.
 Crie uma lista de retângulos e imprima no console:
 A coordenada do centro de cada retângulo, o valor da área e do perímetro.'''

import random
from ponto import Ponto
from retangulo import Retangulo

def main():    
    # for _ in range(random.randint(1,10)):
    #     x_inicial = int(input("X = ")) #x superior esquerdo
    #     y_inicial = int(input("Y = ")) #y superior esquerdo
    #     ponto_sup_esq = Ponto(x_inicial, y_inicial) --------> com input
    
    lista = []
    
    for _ in range(random.randint(1,10)):
        pontinho = Ponto(random.randint(3,15), random.randint(4,16))
        largura = random.randint(3,12)
        altura = random.randint(5,10)
        lista.append(Retangulo(pontinho, largura, altura))

    print('-' * 65)
    #impressão dos dados
    for retangulinho in lista:
        print(retangulinho)

if __name__ == '__main__':
    main()
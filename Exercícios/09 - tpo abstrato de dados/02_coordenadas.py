'''Codifique um Tipo Abstrato de Dados (TAD) chamado Ponto. O tipo criado deverá ter os atributos adequados para a representação do ponto no plano cartesiano. O construtor deverá ser codificado.
 Implemente um método que calcule e retorne a distância entre dois pontos.
 Implemente o método str para retornar a representação de um ponto no formato (x, y).
 Crie uma lista contendo alguns pontos:
 Codifique uma função que calcule a distância de cada ponto em relação a origem.'''

from obj_coordenadas import Ponto
from random import randint

def calcular_distancia_origem(lista_de_pontos: list[Ponto]):
    """Calcula e imprime a distância de cada ponto da lista em relação à origem."""
    
    print('--- Distância à Origem ---')
    print('Ponto (x, y) --> Distância')
    print('--------------------------')
    
    # Itera sobre os objetos Ponto na lista
    for ponto in lista_de_pontos:
        # Chama o método distancia_origem() no objeto 'ponto'
        distancia = ponto.distancia_origem()
        # "Pegue o objeto referenciado por ponto, peça a ele para calcular a sua distância em relação à origem $(0, 0)$, e guarde o valor que ele retornar na variável distancia."
        
        # O método __str__ (chamado implicitamente por f-string/print)
        # retorna a representação "(x, y)" do ponto.
        print(f"{ponto} --> Distância: {distancia:.2f}")


def main():
    # --- Criação da Lista de Pontos ---
    lista_de_pontos = []
    # Cria entre 1 e 5 pontos
    for _ in range(randint(1, 5)):
        # Gera coordenadas aleatórias
        x = randint(0, 9)
        y = randint(0, 9)
        
        # Adiciona o objeto Ponto criado à lista
        lista_de_pontos.append(Ponto(x, y)) 
        
    # --- Execução da Função ---
    calcular_distancia_origem(lista_de_pontos)

    # --- Exemplo de Distância entre Dois Pontos (opcional) ---
    if len(lista_de_pontos) >= 2:
        p1 = lista_de_pontos[0]
        p2 = lista_de_pontos[1]
        
        # Chama o método calcular_dist em p1, passando p2 como argumento
        distancia_p1_p2 = p1.calcular_dist(p2)
        
        print('\n--- Exemplo de Distância entre Dois Pontos ---')
        print(f"Distância entre {p1} e {p2}: {distancia_p1_p2:.2f}")

if __name__ == '__main__':
    main()
    
'''Codifique um Tipo Abstrato de Dados (TAD) chamado Ponto. O tipo criado deverá
ter os atributos adequados para a representação do ponto no plano cartesiano. O
construtor deverá ser codificado.
 Implemente um método que calcule e retorne a distância entre dois pontos.
 Implemente o método str para retornar a representação de um ponto no
formato (x, y).
 Crie uma lista contendo alguns pontos:
 Codifique uma função que calcule a distância de cada ponto em relação a
origem'''


from ponto import Ponto

def main():
    lista = []
    for i in range(3):
        x = int(input(f'X={i+1}'))
        y = int(input(f'Y={i+1}'))
        lista.append(Ponto(x,y))
        
    for pontinho in lista:
        d = pontinho.calcular_dist(Ponto(0,0))
        print(f'Distancia entre o ponto e a origem: {d:.2f}')
    
    
if __name__ =='__main__':
    main()
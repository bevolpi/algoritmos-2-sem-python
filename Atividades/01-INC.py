'''Uma equipe de engenheiros ambientais está analisando o relevo de uma região representada por uma matriz de altitudes. Cada posição da matriz indica a altura do terreno em uma determinada coordenada. Seu objetivo é desenvolver um programa em Python para ajudar a equipe a identificar os pontos mais altos (picos) e os pontos mais baixos (vales) do mapa, considerando a altitude dos vizinhos
ao redor.
Regras: Considere a vizinhança de 8 direções (norte, sul, leste, oeste e diagonais). Para cada célula (i, j) da matriz:
 Se celula[i][j] for maior que todos os seus vizinhos, ela é um pico.
 Se celula[i][j] for menor que todos os seus vizinhos, ela é um vale.
 Caso contrário, é um ponto neutro.
O programa deverá executar as seguintes funcionalidade:
    a) Ler a ordem da matriz a partir do terminal.
    b) Preencher a matriz com valores inteiros aleatórios (utilizar o módulo random). O preenchimento da matriz deverá ocorrer em uma função.
    c) Imprimir a matriz em formato tabular (a impressão deverá ser ocorrer em uma função, diferente da função que fez o preenchimento).
    d) Criar uma nova matriz do mesmo tamanho onde 'P' representa pico, 'V' representa vale e 'N' representa ponto neutro. A geração da matriz deverá ocorrer em uma função.
    e) Imprima no terminal a nova matriz em formato tabular (a impressão deve ocorrer em uma função). Veja um exemplo a seguir.'''
from random import randint


#a e b) criar a matriz
def ler_dados():
    linha = int(input('Informe a quantidade de linhas: '))
    coluna = int(input('Informe a quantidade de colunas: '))
    matriz = [[randint(1, 10)for j in range(coluna)] for i in range(linha)]
    return matriz

#c) impressão tabular
def imprimir_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= "\t")
        print()

#d) criar matriz transformada
def transformar(original):
    v = [[-1,-1], [-1,0], [-1,1],
         [0, -1],         [0, 1],
         [1, -1], [1, 0], [1, 1]]
    transformada = []
    
    for i in range(len(original)):
        aux = []
        
        for j in range(len(original[i])):
            maior = 0
            menor = 0
            vizValido = 0
            valor = original[i][j]
            
            for vi, vj in v:
                ri = i + vi
                rj = j + vj
                
                if ri >= 0 and ri < len(original) and rj >= 0 and rj < len(original[i]):
                    vizValido += 1
                    vizinho = original[ri][rj]
                    
                    if valor > vizinho:
                        maior +=1
                    elif valor < vizinho:
                        menor += 1
                        
                if vizValido > 0:
                    if vizValido == maior:
                        aux.append("P")
                    elif vizValido == menor:
                        aux.append("V")
                    else: 
                        aux.append("N")
                else:
                    print("Sem vizinhos")
                    
        transformada.append(aux)
    return transformada



def main():
    matriz = ler_dados()
    imprimir_matriz(matriz)
    matrizTrans = transformar(matriz)
    imprimir_matriz(matrizTrans)
    
    
    
    
if __name__ == '__main__':
    main()
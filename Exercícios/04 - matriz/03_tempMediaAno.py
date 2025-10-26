'''Análise de Temperaturas Médias Anuais: Você foi contratado para realizar uma análise
simples das temperaturas médias anuais de uma cidade ao longo dos últimos 10 anos. Os
dados são fornecidos em um formato de matriz (array bidimensional), onde cada linha
representa um ano e cada coluna representa um mês (de janeiro a dezembro).
Instruções:
a) Crie uma matriz de 10x12 contendo as temperaturas médias mensais de cada ano (valores
fictícios podem ser utilizados para testar o código).
b) Escreva uma função que calcule a média de cada linha (ano) e retorne uma lista com as
médias.
c) Escreva outra função que determine o ano com a maior média e o ano com a menor média.
d) Implemente um programa principal que utilize essas funções para processar os dados e
imprimir os resultados.
'''
#i = linha
#j = coluna
from random import randint


#a) criar a matriz
def ler_dados():
    total_ano = int(input('Informe o tt de anos: '))
    total_mes = int(input('Informe o tt de meses: '))
    temperatura = [[randint(5, 40)for j in range(total_mes)] for i in range(total_ano)]
    return temperatura


#a) printar a matriz
    # len(matriz) sempre dá o nm de linhas!!!!!
    # len(matriz[i]) dá o de colunas!!
def imprimir_matriz(temperatura):

    for i in range(len(temperatura)):
        for j in range(len(temperatura[i])):
            print(temperatura[i][j], end= "\t")
        print()
    

# b) fazer a media anual como lista
def calcular_media(temperatura):
    media = []
    for i in range(len(temperatura)):
        soma = 0
        for j in range(len(temperatura[i])):
            soma = soma + temperatura[i][j]
        media.append(soma / len(temperatura[i]))
    return media # aqui precisa printar la embaixo!!!!! pq retorna 1 valor e nao tem print

# b) printar a média
def imprimir_media(media): 
    for i in range(len(media)):
        print(f'Ano {i + 1} --> {media[i]:.2f}') 
    
# c) ano com a maior média
def calcular_maior_media(media_anual):
    maior_media = media_anual[0]
    ano = 0
    for i in range(len(media_anual)):
        if media_anual[i] > maior_media:
            maior_media = media_anual[i]
            ano = i
    return ano

def calcular_menor_media(media_anual):
    menor_media = media_anual[0]
    ano = 0
    for i in range(len(media_anual)):
        if media_anual[i] < menor_media:
            menor_media = media_anual[i]
            ano = i
    return ano


def main():
    #a) imprimir
    temperatura = ler_dados()
    imprimir_matriz(temperatura)
    #b) média
    media_anual = calcular_media(temperatura)
    print("Média anual: ")
    imprimir_media(media_anual)
    #c) maior e menor
    ano_maior_media = calcular_maior_media(media_anual)
    print(f'Ano com a maior média de temperatura {(ano_maior_media + 1)}')
    ano_menor_media = calcular_menor_media(media_anual)
    print(f'Ano com a menor média de temperatura {(ano_menor_media + 1)}')
    

if __name__ == '__main__':
    main()
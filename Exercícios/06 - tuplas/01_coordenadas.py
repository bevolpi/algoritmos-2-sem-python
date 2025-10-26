'''Implemente uma função em Python que recebe uma lista de tuplas, onde cada
tupla representa as coordenadas (x, y) de um ponto no plano cartesiano. A
função deve gerar e imprimir no terminal as seguintes informações:
a) O ponto mais distante da origem (0, 0).
b) O ponto mais próximo da origem (0, 0).
c) A média das distâncias dos pontos à origem.
Para calcular a distância de um ponto p de coordenas (x, y) até a origem (0, 0)
utiliza-se a expressão:
d = sqrt((x ** 2) + (y ** 2))'''

from math import sqrt

def ler_dados():
    plano = []
    qtde = int(input("Quantos pontos? "))
    for i in range(qtde):
        ponto = (int(input(f"X{i} = ")), int(input(f"Y{i} = ")))
        plano.append(ponto)
    return plano

def longe(lista):
    distancia = []
    for i in range(len(lista)):
        x, y = lista[i]
        distancia.append(sqrt((x**2) + (y**2)))
    ponto = lista[0]
    maior = distancia[0]
    for i in range(len(lista)):
        if distancia[i] > maior:
            maior = distancia[i]
            ponto = lista[i]
    return ponto

def perto(lista):
    distancia = []
    for i in range(len(lista)):
        x, y = lista[i]
        distancia.append(sqrt((x**2) + (y**2)))
    ponto = lista[0]
    menor = distancia[0]
    for i in range(len(lista)):
        if distancia[i] < menor:
            menor = distancia[i]
            ponto = lista[i]
    return ponto

def media(plano):
    soma = 0
    for coordenada in plano: 
        x, y = coordenada
        dist = sqrt((x**2) + (y**2))
        soma += dist
    media = soma / len(plano)
    return media        

def main():
    lista = ler_dados()
    print(lista)
    
    distante = longe(lista)
    print(distante)
    proximo = perto(lista)
    print(proximo)
    
    mediaD = media(lista)
    print(mediaD)
    
    
    
    
if __name__ == '__main__':
    main()
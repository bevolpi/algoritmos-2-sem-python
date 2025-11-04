'''Implemente uma função em Python que recebe uma lista de tuplas, onde cada tupla representa as coordenadas (x, y) de um ponto no plano cartesiano. A função deve gerar e imprimir no terminal as seguintes informações:
a) O ponto mais distante da origem (0, 0).
b) O ponto mais próximo da origem (0, 0).
c) A média das distâncias dos pontos à origem.
Para calcular a distância de um ponto p de coordenas (x, y) até a origem (0, 0)
utiliza-se a expressão:
d = sqrt((x ** 2) + (y ** 2))'''

from random import randint
from math import sqrt

#função p gerar lista de pontos 
def gerar_pontos():
    lista = list()
    for _ in range(randint(1, 5)):
        lista.append((randint(-10, 10), randint(-10, 10)))
    return lista

# função para calcular a distância de cada um dos pontos até a origem
def calcular_distancia(lista):
    distancia = []
    for i in range(len(lista)):
        x, y = lista[i]
        distancia.append(sqrt((x**2) + (y**2)))
    return distancia

# função p retornar ponto mais distante
def maisDistante(lista, distancia):
    ponto = lista[0]
    maior = distancia[0]
    for i in range(len(lista)):
        if distancia[i] > maior:
            maior = distancia[i]
            ponto = lista[i]
    return ponto

# função para retornar o ponto mais distante da origem

def maisProximo(lista, distancia):
    ponto = lista[0]
    menor = distancia[0]
    for i in range(len(lista)):
        if distancia[i] < menor:
            menor = distancia[i]
            ponto = lista[i]
    return ponto

def calcularMedia(distancia):
    media = 0
    for d in distancia:
        media += d
    return media / len(distancia)

def main():
    lista = gerar_pontos()
    print(f"Lista de coordenadas: {lista}")
    distancia = calcular_distancia(lista)
    for i in range(len(lista)):
        print(f" {lista[i]} --> {distancia[i]:.2f}")
        
    print(f"Ponto + distante: {maisDistante(lista, distancia)}")
    print(f"Ponto + próximo: {maisProximo(lista, distancia)}")
    print(f"Média das distâncias: {calcularMedia(distancia):.2f}")
    
if __name__ == '__main__':
    main()
    
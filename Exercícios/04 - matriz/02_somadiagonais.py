'''Escreva um programa em Python que preencha uma matriz quadrada de ordem 4 com
valores inteiros aleatórios. Em seguida:
a) Mostre a soma dos elementos da diagonal principal (dp).
b) Mostre a soma dos elementos da diagonal secundárian (ds).
'''
#selmini way
from random import randint

dp = 0
ds = 0
#lendo os valores da matriz
matriz = [[randint(1, 10)for i in range(4)] for i in range(4)]
'''print(matriz)'''
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end= "\t")
    print()
#soma os elementos da diagonal principal e  da secundária
#     o len(matriz) me dá o total de LINHAS!
#     2 laços garante que vai passar por todos os números da matriz
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            dp += matriz [i][j]
        if i + j == len(matriz) - 1:
            ds += matriz[i][j]
        
print(f" soma dos elementos da DP: {dp}")
print(f" soma dos elementos da DS: {ds}")

'''Escreva um programa em Python que preencha um matriz quadrada de ordem 5
com valores aleatórios. Em seguida, troque os elementos da diagonal principal com
os elementos da diagonal secundária. Como exemplo, considere a matriz quadrada
de ordem 3.'''
from random import randint

#criar a matriz
matriz = [[randint(1, 10)for j in range(3)] for i in range(3)]
#printar a matriz
def imprimir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= "\t")
        print()
        
print("Impressão original")
imprimir(matriz)
    
j = len(matriz)-1
for i in range(len(matriz)):
    aux = matriz[i][i]
    matriz[i][i] = matriz [i][j]
    matriz [i][j] = aux
    j -= 1

print()

print("Impressão trocada")
imprimir(matriz)

'''ihan'''
# from random import randint

# m = [[ randint(0,10) for j in range(4)] for i in range(4)]

# for i in range(len(m)):
#     for j in range (len(m)):
#         print(m[i][j],end="\t")
#     print("\n")
    
# contador = 0
# for i in range(len(m)):
#     for j in range (len(m)):
#         if((i+j) == (len(m)-1)):
#             aux = m[contador][contador]
#             m[contador][contador] = m[i][j]
#             m[i][j] = aux
#             contador+=1
            
            
# print("Revelação")
# for i in range(len(m)):
#     for j in range (len(m)):
#         print(m[i][j],end="\t")
#     print("\n")

'''isso serve p achar as matrizes '''
# dp = []
# ds = []
# matriz = [[randint(1, 10)for i in range(3)] for i in range(3)]
# for i in range(len(matriz)):
#     for j in range(len(matriz)):
#         print(matriz[i][j], end= "\t")
#     print()

# for i in range(len(matriz)):
#     for j in range(len(matriz)):
#         if i == j:
#             dp.append(matriz[i][j])
#         if i + j == len(matriz) - 1:
#             ds.append(matriz[i][j])

# print(dp, end= "\t")
# print()
# print(ds, end= "\t")
        
            
        

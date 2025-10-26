# linha = int(input("Número de linhas --> "))
# coluna = int(input("Número de coluna --> "))

# matriz = []
# #controle de linha
# for y in range(linha):
#     aux = [] #são as linhas que eu crio p depois adicioná-las na matriz
#     #controle de coluna
#     for x in range(coluna):
#         aux.append(int(input("Valor --> ")))
#     matriz.append(aux)

# print(matriz)

'''OUUU'''

linha = int(input("Número de linhas --> "))
coluna = int(input("Número de coluna --> "))
#  -> tenta fazer o print q deixei lá embaixo p entender. 
matriz = [[int(input("valor: ")) for x in range(coluna)] for y in range(linha)]

print(matriz)



'''LINHA DE RACIOCÍNIO DO EX DE CIMA'''
'''dependendo do número de linhas, o 1° for cria, por ex, 3 "[]" vazios'''
# linha = int(input("Número de linhas --> "))
# coluna = int(input("Número de coluna --> "))

# matriz = [[] for y in range(linha)]

# print(matriz)
'''----------'''
'''mas aí precisamos colocar algum valor, ent dentro do "[]", colocamos um 2° for'''
# linha = int(input("Número de linhas --> "))
# coluna = int(input("Número de coluna --> "))

# matriz = [[0 for x in range(coluna)] for y in range(linha)]

# print(matriz)
'''----------'''
'''agora vai p cima com o resultado final'''

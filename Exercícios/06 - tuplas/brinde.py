'''Implemente uma função em Python que recebe uma lista de tuplas, onde cada tupla representa um intervalo numérico [a,b], com a ≤ b. A função deve realizar as seguintes operações:
a) unir intervalos que se sobrepõem: se dois intervalos [a, b] e [c, d] se sobrepõem (ou seja, b ≥ c), eles devem ser unidos em um único intervalo.
    [(2,4), (1,3)] -> sobrepondo e transformando em 1 único intervalo = (1,4)
b) contar o número total de intervalos resultantes.
c) Retornar a soma total do comprimento de todos os intervalos resultantes.
'''

lista = [(2,4), (1,3), (3,5), (7,10)]
aux_a, aux_b = lista[0]
intervalo = []

for i in range(len(lista)): 
    a,b = lista[i]
    if a < aux_b:
        if b > aux_b:
            aux_b = b
    if b < aux_b:
        if a < aux_a:
            aux_a = a
    intervalo.append((aux_a, aux_b))

print(intervalo)

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
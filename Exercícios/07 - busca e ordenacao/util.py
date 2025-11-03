# esse arquivo não executa pq ele é um módulo

# função para realizar a busca linear em uma lista numérica. A função deve receber como parâmetro a lista e o valor a ser localizado.

def buscar(lista:list[int], valor:int) -> int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
        else: 
            return -1

#função para ordenar uma lista de números inteiros em ordem crescente usando o método bolha(bubblesort)

def ordenar(lista:list[int])-> list[int]:
    for _ in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                # aux = lista[i]
                # lista[i] = lista[i+1]
                # lista[i+1] = aux
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

def buscar_ord(lista:list[int], valor: int) -> int:
    procura = len(lista)//2
    ...
        
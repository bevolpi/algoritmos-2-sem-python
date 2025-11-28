# esse arquivo não executa pq ele é um módulo

# função para realizar a busca linear em uma lista numérica. A função deve receber como parâmetro a lista e o valor a ser localizado.

def buscar(lista:list[int], valor:int) -> int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
        else: 
            return -1


# https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
#função para ordenar uma lista de números inteiros em ordem crescente usando o método bolha(bubblesort)
#percorre toda a lista todas as vezes (se o i0 > i1 troca, se i0>i2 troca.... assim com todos)

def bubble_sort(lista:list[int])-> list[int]:
    for _ in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                # aux = lista[i]
                # lista[i] = lista[i+1]
                # lista[i+1] = aux
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

#função para ordenar uma lista com método seleção
#ve se o i0 >ifinal, se for, troca e "descarta" o menor, dps, ve se o i1> ifinal...) 

def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
            
        # Troca os elementos (essa linha precisa estar dentro do laço externo)
        lista[i], lista[menor] = lista[menor], lista[i]

#função para ordenar uma lista pelo método de inserção
#2 variáveis, se for menor, joga o número p outra váriavel
def insertion_sort(lista):
    n = len(lista)
    for j in range(1, n):
        valor = lista[j]
        i = j - 1
        while i >= 0 and valor < lista[i]:
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = valor

#função para ordenar uma lista pelo método quicksort (pivô como último elemento)
def quick_sort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    
    if inicio < fim:
        pivo = particionar(lista, inicio, fim) #particionar = dividir
        quick_sort(lista, inicio, pivo - 1)
        quick_sort(lista, pivo + 1, fim)

# continuando o quicksort -> precisa de 2 funções    
def particionar(lista, inicio, fim) -> int:
    pivo = lista[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j] <= pivo: 
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
            
    #coloca o pivô no local correto
    lista[i+1], lista[fim] = lista[fim], lista[i+1]
    return i + 1


def buscar_ord(lista:list[int], valor: int) -> int:
    procura = len(lista)//2
    ...
        
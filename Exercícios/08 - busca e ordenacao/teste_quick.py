# função para ordenar uma lista pelo método quicksort (pivô como último elemento)
def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio < fim:
        pivo = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1)
        quicksort(lista, pivo + 1, fim)

# continuando o quicksort -> precisa de 2 funções
def particionar(lista, inicio, fim) -> int:  # retorna o índice do pivô
    pivo = lista[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    # coloca o pivô no local correto
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

# 1. Criação da Lista Desordenada
minha_lista_desordenada = [10, 7, 8, 4, 1, 5]

print(f"Lista antes da ordenação: {minha_lista_desordenada}")

# 2. Chamada da Função Quick Sort
# Você só precisa passar o nome da lista.
quicksort(minha_lista_desordenada) 

# 3. Verificação do Resultado
# A lista original foi modificada (ordenada)
print(f"Lista depois da ordenação: {minha_lista_desordenada}")
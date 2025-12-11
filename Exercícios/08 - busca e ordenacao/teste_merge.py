
def mergesort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    esquerda_ordenada = mergesort(esquerda)
    direita_ordenada = mergesort(direita)
    
    return juntar_listas(esquerda_ordenada, direita_ordenada)


def juntar_listas(esq, dir):
    i = 0  # índice da lista da esquerda (para ninguém fazer confusão entre os índices)
    j = 0  # índice da lista da direita
    resultado = []
    
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    # cuidado: é importante verificar se sobre algum elemento na 
    # lista da esquerda ou na da direita. Se sobrar algum elemento,
    # acrescenta no final da lista
    while i < len(esq):
        resultado.append(esq[i])
        i += 1

    while j < len(dir):
        resultado.append(dir[j])
        j += 1

    return resultado

# 1. Criação da Lista Desordenada
minha_lista_desordenada = [10, 7, 8, 4, 1, 5]

print(f"Lista antes da ordenação: {minha_lista_desordenada}")

# 2. Chamada da Função Quick Sort
# Você só precisa passar o nome da lista.
mergesort(minha_lista_desordenada) 

# 3. Verificação do Resultado
# A lista original foi modificada (ordenada)
print(f"Lista depois da ordenação: {minha_lista_desordenada}")
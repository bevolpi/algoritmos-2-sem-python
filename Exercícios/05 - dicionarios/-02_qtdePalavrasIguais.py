'''A partir de uma lista de palavras (que pode haver repetição), imprimir a qtde de vezes que cada a palavra aparece. E a ocorrencia de cada letra'''

lista = []
total = int(input("Qual o total de palavras? "))

for i in range(total):
    lista.append(input("Palavra: "))
    
# contar o numero de ocorrências de cada uma das palavras
ocorrencia = {}
for palavra in lista:
    if palavra in ocorrencia:
        ocorrencia[palavra] += 1
    else:
        ocorrencia[palavra] = 1
        
# imprimir ocorrencia das palavras: 
# for chave, valor in dicionario.items():
print("Ocorrencia das palavras:")
for palavra, qtde in ocorrencia.items():
    print(f"\n{palavra} -> {qtde} vezes")
    
# ocorrencia das letras
print("\nOcorrencia das letras:")
ocorrencia_letra = {}
for palavra in lista:
    for letra in palavra:
        if letra in ocorrencia_letra:
            ocorrencia_letra[letra] += 1 
        else: 
            ocorrencia_letra[letra] = 1

# imprimir ocorrencia letra
for letra, qtde in ocorrencia_letra.items():
    print(f"{letra} -> {qtde} vezes")
    
'''Escreva um programa para criar uma nova string composta pelo primeiro, meio e último caractere de uma string de entrada.'''
# a = input("Insira a string: ")
# ult = len(a)
# meio = int(ult/2)
# res = a[0] + a[meio] + a[ult-1] #precisa ser len - 1, pq o nm da len é sempre omitido

# print(res)

'''Escreva um programa para criar uma nova string composta pelos três caracteres do meio de uma string de entrada.'''
# a = input("Insira a string: ")
# l = len(a)
# meio = int(l/2)
# res = a[meio-1] + a [meio] + a[meio + 1]

# print(res)

'''Dadas duas strings, s1 e s2, escreva um programa para criar uma nova string s3adicionando s2 no meio de s1.'''

# s1 = input("Insira a string: ")
# s2 = input("Insira a string: ")

# meio = int(len(s1)/2)

# s1i = s1[:meio]
# s1f = s1[meio:]

# res = s1i + s2 + s1f
# print(res)

'''A string dada contém uma combinação de letras maiúsculas e minúsculas. Escreva um programa para organizar os caracteres da string de forma que todas as letras minúsculas venham primeiro.'''

# a = 'PyNaTive'
# lower = ''
# upper = ''

# for char in a:
#     if char.islower():
#         lower += char
#     else:
#         upper += char

# result = lower + upper
# print(result)  

'''Conte todas as letras, dígitos e símbolos especiais de uma determinada sequência de caracteres.'''

# str1 = "P@#yn26at^&i5ve"
# l = 0
# d = 0
# s = 0

# for letra in str1:
#     if letra.isalpha():
#         l += 1
#     elif letra.isdigit():
#         d += 1
#     else:
#         s +=1
        
# print(f"Letras = {l}\n" + 
#       f"Números = {d}\n" 
#       f"Símbolos = {s}")

'''Dadas duas strings, s1 e s2, escreva um programa para criar uma nova string s3 composta pelo primeiro caractere de s1, seguido pelo último caractere de s2, depois pelo segundo caractere de s1 e o penúltimo caractere de s2, e assim por diante. Quaisquer caracteres restantes devem ser adicionados ao final do resultado.'''

# s1 = "Abc"
# s2 = "Xyz"
# s3 = ""
# s1_length = len(s1)
# s2_length = len(s2)

# length = s1_length if s1_length > s2_length else s2_length

# for i in range(length):
#     s3 += s1[i] + s2[i]
    
# print(s3)

'''Escreva um programa para verificar se duas strings estão balanceadas. Por exemplo, as strings s1 e s2 estão balanceadas se todos os caracteres de s1 estiverem presentes em s2. A posição do caractere não importa.'''

# s1 = "Ynf"
# s2 = "PYnative"
# res = 0
# for i in range(len(s1)):
#     if s1[i] not in s2:
#         res +=1
# if res > 0:
#     print("Falso")
# else:
#     print("Vdd")

'''Escreva um programa para encontrar todas as ocorrências de "USA" em uma determinada string, ignorando maiúsculas e minúsculas.'''

# str1 = "Welcome to USA. usa awesome, isn't it?".lower()
# contar = str1.count("usa")

# print(contar)


'''Dada uma string s1, escreva um programa para retornar a soma e a média dos dígitos que aparecem na string, ignorando todos os outros caracteres.'''

# str1 = "PYnative29@#8496"
# digitos = 0
# soma = 0
# for nm in str1:
#     if nm.isdigit():
#         digitos += 1
#         soma += int(nm)
# media = soma / digitos

# print(f"{media:.2f}")

'''Escreva um programa para contar as ocorrências de todos os caracteres em uma string.'''
# str1 = "Apple"
# ocorrencia = {}

# for letra in str1:
#     if letra not in ocorrencia:
#         ocorrencia[letra] = 1
#     else:
#         ocorrencia[letra] += 1

# print(ocorrencia)

'''Escreva um programa para encontrar a última posição da substring " Emma " em uma string dada.'''

# texto = "Emma é boa. Emma é inteligente. Emma é gentil."
# substring = "Emma"

# ultima_posicao = -1 

# for i in range(len(texto) - len(substring) + 1):
#     if texto[i:i + len(substring)] == substring:
#         ultima_posicao = i  # atualiza sempre que encontrar

# if ultima_posicao != -1:
#     print(f"A última posição de '{substring}' é: {ultima_posicao}")
# else:
#     print(f"'{substring}' não foi encontrada na string.")
    
'''Escreva um programa para dividir uma string dada em hífens e exibir cada substring.'''

# str1 = "Emma-is-a-data-scientist"

# print("Exibindo cada substring:\n")

# palavra_atual = ""

# for char in str1:
#     if char != "-":          # Se o caractere não é hífen, faz parte da palavra
#         palavra_atual += char
#     else:                    # Se encontrar um hífen, a palavra acabou
#         print(palavra_atual)
#         palavra_atual = ""   # Reinicia para começar a próxima palavra

# # Após o loop, imprime a última palavra (pois não há hífen no fim)
# if palavra_atual:
#     print(palavra_atual)


'''Remover símbolos especiais/pontuação de uma string'''

# str1 = "/*Jon is @developer & musician"
# res = ""
# ultimo_foi_espaco = False

# for letra in str1:
#     if letra.isalnum():
#         res += letra
#         ultimo_foi_espaco = False
#     elif letra == " " and not ultimo_foi_espaco:
#         res += letra
#         ultimo_foi_espaco = True

# print(res)

'''Escreva um programa para encontrar palavras que contenham letras e números a partir de uma string de entrada.'''
# str1 = "Emma25 is Data scientist50 and AI Expert123"

# palavra = ""
# tem_letra = False
# tem_numero = False

# for char in str1 + " ":  # adiciona um espaço no final para garantir a última palavra
#     if char != " ":
#         palavra += char
#         if char.isalpha():
#             tem_letra = True
#         elif char.isdigit():
#             tem_numero = True
#     else:
#         # fim de uma palavra → verificar se tem letra e número
#         if palavra and tem_letra and tem_numero:
#             print(palavra)
#         # reinicia para a próxima palavra
#         palavra = ""
#         tem_letra = False
#         tem_numero = False

'''O desafio consiste em criar uma função que irá receber um texto (string) e retornará a palavra mais longa.'''

# def longa(str1):
#     # Remove quebras de linha e separa por espaços
#     palavras = str1.replace("\n", " ").split()
#     maior = ""
#     for palavra in palavras:
#         if len(palavra) > len(maior):
#             maior = palavra
            
#     print(maior)

# str1 = """No meu computador,
# o Python habita
# e com ele eu desvendo
# a lógica aaaaaaaaaaaaaaaaaaainfinita
# Nas linhas de código
# encontro o meu ser
# e através da sintaxe
# posso me conhecer"""

# longa(str1)


'''O desafio consiste em ordenar uma lista de títulos de livros em ordem alfabética e deixá-los separados por vírgula.'''

# titulos = """O Senhor dos Anéis
# Harry Potter e a Pedra Filosofal
# 1984
# Macunaíma"""

# lista_titulos = titulos.split("\n")

# # 2️⃣ Ordenar manualmente (bubble sort, sem sort())
# n = len(lista_titulos)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if lista_titulos[j].lower() > lista_titulos[j + 1].lower():
#             lista_titulos[j], lista_titulos[j + 1] = lista_titulos[j + 1], lista_titulos[j]

# # 3️⃣ Mostrar separados por vírgula (sem join)
# print("Títulos ordenados:")
# for i in range(len(lista_titulos)):
#     print(lista_titulos[i], end="")
#     if i < len(lista_titulos) - 1:
#         print(", ", end="")

# print()  # quebra de linha no final

'''Contar quantas vezes uma determinada palavra aparece na lista de títulos (artigos).'''

artigos = [
'RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text',
'VideoLLM: Modeling Video Sequence with Large Language Models',
'Watermarking Text Data on Large Language Models for Dataset Copyright Protection',
'InheritSumm: A General, Versatile and Compact Summarizer by Distilling from GPT',
'Can Large Language Models emulate an inductive Thematic Analysis of semi-structured interviews? An exploration and provocation on the limits of the approach and the model',
'GPT-SW3: An Autoregressive Language Model for the Nordic Languages',
'The Emergence of Economic Rationality of GPT',
'Can We Edit Factual Knowledge by In-Context Learning?',
'G3Detector: General GPT-Generated Text Detector',
'GPT Paternity Test: GPT Generated Text Detection with GPT Genetic Inheritance'
]

palavra = "GPT"
contador_total = 0

for titulo in artigos:
    # divide o título em partes e percorre cada palavra
    palavras_titulo = titulo.split()
    for termo in palavras_titulo:
        if palavra.lower() in termo.lower():
            contador_total += 1

print(f"A palavra '{palavra}' aparece {contador_total} vezes no total.")

'''Escreva uma função, chamada contaVoigais, que conta todas as vogais presentes no texto recebido como parâmetro e retorna um dicionário contendo a quantidade de cada vogal. Escreva um programa a fim de testar sua função, e exiba, no fim, os dados do dicionário retornado.'''

def contaVogais(texto):
    cont = {}
    for letra in texto:
        if letra in 'aeiou':
            if letra in cont:
                cont[letra] += 1
            else:
                cont[letra] = 1
    return cont

texto = input()
vogais = contaVogais(texto)
for i in vogais:
    print("qtde...")
'''Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções: ­

incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones. ­
incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-­lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. ­
excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda. ­
excluirNome – essa função exclui uma pessoa da agenda. ­
consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.'''
dicio = {}
def incluirNovoNome(nome, numeros):
    dicio[nome] = numeros

def incluirTelefone(nome, numero):
    if nome in dicio:
        dicio[nome].append(numero)
    else:
        incluirNovoNome(nome, [numero])

def excluirNome(nome):
    if nome in dicio:
        del dicio[nome]
    
def excluirTelefone(nome, telefone):
    if nome in dicio:
        if telefone in dicio[nome]:
            dicio[nome].remove(telefone)
    if dicio[nome] == []:
        excluirNome(nome)
        
def consultarTelefone(nome):
    if nome in dicio:
        return dicio[nome]
    
    
    
titulos = ["O Senhor dos Anéis", "Harry Potter", "", "A Revolução dos Bichos", ""]
linhas = titulos.split("\n")   # divide em linhas
lista_titulos = []             # lista final

for t in linhas:
    titulo_limpo = t.strip()   # remove espaços extras
    if titulo_limpo:           # só adiciona se não for vazio
        lista_titulos.append(titulo_limpo)
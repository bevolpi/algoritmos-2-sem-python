'''Uma rainha requisitou os serviços de um monge e disse-lhe que pagaria qualquer
preço. O monge, necessitando de alimentos, perguntou à rainha se o pagamento
poderia ser feito com grãos de trigo dispostos em um tabuleiro de xadrez (64 casas), de tal
forma que o primeiro quadro contivesse apenas um grão e os quadros
subsequentes, o dobro do quadro anterior. A rainha considerou o pagamento
barato e pediu que o serviço fosse executado, sem se dar conta de que seria
impossível efetuar o pagamento. Escreva um programa em Python para calcular o
número de grãos de trigo que o monge deverá receber. O programa deverá ter
uma função para calcular e retornar o número de grãos de trigo. O cálculo deve
ser realizado por meio de um laço de repetição for.'''

# função principal
#   "->" é a documentação, p qnd usar, saber qual tipo de valor q a def retorna
#   "-> None" significa q nao retorna nenhum valor
def calcular() -> int:
    total = 0
    i = 0
    for i in range(64):
        total += 2 ** i
    return total

# programa principal
total = calcular()
print(f"Total de grãos: {total}")
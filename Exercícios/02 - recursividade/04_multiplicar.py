# '''A multiplicação entre dois números inteiros pode ser definida em função da
# operação primitiva soma. Escreva um programa em Python que leia dois valores
# inteiros m e n e calcule a multiplicação (sem utilizar o operador *) entre eles.'''

def multiplicacao(a:int, b:int) -> int:
    if b == 0: return 0
    if b>0: return a + multiplicacao(a, b-1)
    return -multiplicacao(a,-b)

# função principal -> entrada e saída de dados
def main():
    a = int(input('A = '))
    b = int(input('b = '))
    print(f"{a} * {b} = {multiplicacao(a,b)}")

# programa principal
if __name__ == '__main__':
    main()
   
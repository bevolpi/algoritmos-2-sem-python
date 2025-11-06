'''Implemente um conjunto de funções que manipulem números complexos representados por tuplas. Cada tupla representará um número complexo no formato (a, b), onde: a é a parte real do número complexo e b é a parte imaginária do número complexo.
Requisitos:
a) Soma de números complexos: crie uma função somar(c1, c2) que recebe duas tuplas representando números complexos e retorna uma tupla que é a
soma dos dois. A soma entre (a + bi) e (c + di) = (a + c) + (b + d) * i.
b) Multiplicação de números complexos: crie uma função multiplicar(c1, c2) que recebe duas tuplas e retorna a multiplicação dos dois números
complexos. A multiplicação entre (a + bi) e (c + di) = (ac - bd + ad + bc) * i.
c) Módulo de um número complexo: crie uma função modulo(c) que recebe uma tupla representando um número complexo e retorna o módulo desse
número. O módulo do número complexo (a + bi) é dado por sqrt(a**2 + b ** 2)
d) Exibir número complexo: crie uma função exibir(c) que recebe uma tupla representando um número complexo e exibe o número no formato correto a + bi.
'''
# função para realizar a soma --> (a + bi) + (c + di) = (a + c, b + d)
def somar(c1, c2):
    a, b = c1
    c, d = c2
    real = a + c
    imag = b + d
    return (real, imag)

# função para realizar a multiplicação --> (a + bi)(c + di) = (ac - bd, ad + bc)
def multiplicar(c1, c2):
    a, b = c1
    c, d = c2
    real = (a * c) - (b * d)
    imag = (a * d) + (b * c)
    return (real, imag)

# função para imprimir o número complexo no formato pedido no enunciado do exercício
def exibir_complexo(c):
    a, b = c
    print(f"{a} + {b}i")

# função principal --> sempre chamada a partir do programa principal
def main():
    z1 = (3, 2)   # 3 + 2i
    z2 = (1, 4)   # 1 + 4i

    s = somar(z1, z2)
    m = multiplicar(z1, z2)

    print("Soma:")
    exibir_complexo(s)

    print("Multiplicação:")
    exibir_complexo(m)

# programa principal
if __name__ == "__main__":
    main()
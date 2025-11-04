'''Implemente um conjunto de funções que manipulem números complexos representados por tuplas. Cada tupla representará um número complexo no
formato (a, b), onde: a é a parte real do número complexo e b é a parte imaginária do número complexo.
Requisitos:
a) Soma de números complexos: crie uma função somar(c1, c2) que recebe duas tuplas representando números complexos e retorna uma tupla que é a
soma dos dois. A soma entre (a + bi) e (c + di) = (a + c) + (b + d) * i.
b) Multiplicação de números complexos: crie uma função multiplicar(c1, c2) que recebe duas tuplas e retorna a multiplicação dos dois números
complexos. A multiplicação entre (a + bi) e (c + di) = (ac - bd + ad + bc) * i.
c) Módulo de um número complexo: crie uma função modulo(c) que recebe uma tupla representando um número complexo e retorna o módulo desse
número. O módulo do número complexo (a + bi) é dado por sqrt(a**2 + b ** 2)
d) Exibir número complexo: crie uma função exibir(c) que recebe uma tupla representando um número complexo e exibe o número no formato correto a + bi.
'''

def main():
    c1 = (3, 2)     # 3 + 2i
    c2 = (1, -4)    # 1 - 4i
    c3 = (-2, 5)    # -2 + 5i
    c4 = (0, -3)    # 0 - 3i
    c5 = (7, 0)     # 7 + 0i

    # Podemos guardar em uma lista
    numeros_complexos = [c1, c2, c3, c4, c5]
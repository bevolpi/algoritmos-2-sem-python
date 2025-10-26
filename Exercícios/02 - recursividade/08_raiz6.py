'''Analise a sequência a seguir. Definia uma função recursiva.
𝐴1 = sqrt(6)
𝐴2 = sqrt(6 + sqrt(6))
𝐴3 = sqrt(6 + sqrt(6 + sqrt(6)))
𝐴4 = ...'''

from math import sqrt

def raiz6(n: int) -> int:
    if n == 1: return sqrt(6)
    return sqrt(6 + raiz6(n-1))

def main():
    n = int(input("n = "))
    if n <= 0:
        print("nao pode")
    else:
        print(f"A{n} = {raiz6(n)}")
    
if __name__ == "__main__":
    main()
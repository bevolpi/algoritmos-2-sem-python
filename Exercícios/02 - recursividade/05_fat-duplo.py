'''O fatorial duplo de um número natural n é o produto de todos os números de 1
(ou 2) até n, contados de 2 em 2.Por exemplo, o fatorial duplo de 8 é 8 × 6 × 4 ×
2 = 384, e o fatorial duplo de 7 é 7 × 5 × 3 × 1 = 105. Defina uma função para
calcular o fatorial duplo usando recursividade'''

def fatorial_duplo(n):
    if n == 1: return 1
    if n == 2: return 2
    else:
        return n * fatorial_duplo(n-2)


def main():
    n = int(input("Insira um nm: "))
    if n <= 0:
        print("nao pode")
    else:
        print(f"fatorial de {n} = {fatorial_duplo(n)}")
    
if __name__ == "__main__":
    main()
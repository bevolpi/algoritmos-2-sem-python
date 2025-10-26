'''Escreva um programa em PY que tenha um método recursivo que calcule o n-
ésimo número de Pell.
p(n)= 
        1                     se n = 0
        2                     se n = 1
        2p(n - 1) + p(n - 2)  se n ≥ 2'''

def pell(n):
    if n == 1: return 0
    if n == 2: return 1
    return 2 * pell(n-1) + pell(n - 2)

def main():
    n = int(input("n = "))
    if n <= 0:
        print("nao pode")
    else:
        print(f"A{n} = {pell(n)}")
    
if __name__ == "__main__":
    main()
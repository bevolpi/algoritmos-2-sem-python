# Escreva um programa em Python que contenha um método recursivo que calcule o valor de x^n. O valor de n deve ser maior ou igual a 0

def calcular(x: int, n:int) -> int:
    if n == 0: return 1
    return x * (calcular(x, n-1)) 

    
def main():
    x = int(input("Insira nm (x): "))
    n = int(input("Insira nm int e positiv(n): "))
    if n <= 0:
        print("Não pode - int positiv")
    else: 
        print(f"{x}^{n} = {calcular(x, n)}")

if __name__ == "__main__":
    main()
    
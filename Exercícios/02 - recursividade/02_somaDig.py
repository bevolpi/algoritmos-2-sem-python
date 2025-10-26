#Escreva um programa em Python que tenha um método recursivo que calcule a soma dos dígitos de um número inteiro informado via teclado
#método = função

def somar(n: int) -> int:
    if n == 0: return 0
    return n % 10 + somar(n // 10)

def main():
    n = int(input("Insira nm int e positiv: "))
    if n <= 0:
        print("Não pode - int positiv")
    else: 
        print(f"Soma dos dígitos de {n} = {somar(n)}")

if __name__ == "__main__":
    main()
    
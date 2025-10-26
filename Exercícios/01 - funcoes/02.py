'''Considere o seguinte algoritmo escrito em pseudolinguagem.
1. input n
2. print n
3. if n = 1 then STOP
4. if n é ímpar then n ← 3n + 1
5. else n ← n/2
6. GOTO 2
Considerando que a entrada seja o número 22, a seguinte sequência será impressa no vídeo:
22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
Escreva um programa em Python para implementar o problema descrito.'''

# função paa imprmir os valores
def imprimir(n: int) -> None:
    while True:
        print(f"{n}", end=" ")
        if n == 1:
            break
        elif n % 2 != 0:
            n = 3*n + 1
        else:
            n = n // 2
            
# função principal -> main
def main() -> None:
    n = int(input("Escreva um número: "))
    imprimir(n)

# programa principal
if __name__ == "__main__":
    main()
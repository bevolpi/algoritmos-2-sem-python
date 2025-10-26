# função mdc --> p calcular e retornar o máx divisor comum
def mdc(m: int, n: int) -> int:
    if n > m:
        return mdc(n, m)
    elif n==0: #-> caso base
        return m
    return mdc(n, m % n)

# função principal -> entrada e saída de dados
def main():
    m = int(input('M = '))
    n = int(input('N = '))
    print(f"mdc({m}, {n}) = {mdc(m,n)}")

# programa principal
if __name__ == '__main__':
    main()
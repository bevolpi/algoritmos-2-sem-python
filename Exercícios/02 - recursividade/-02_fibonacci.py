# programa com função resursiva p ler um valor int e positivo e retorne o valor de fibonacci (soma dos 2 anteriores) na posição indicada
# o usuário informará a posição do número e não o número em si

# ESSE É UM MAL EXEMPLO RECURSIVO -> CONSOME MTA MEMÓRIA!!!
'''
def fibonacci_iterativo(p: int) -> int:
    if p == 1 or p == 2:
        return 1
    x, y = 1, 1
    for _ in range(3, p + 1):
        x, y = y, x + y
    return y
'''
        
# função fibonacci
def fibonacci_recursivo(p: int) -> int:
    if p == 1 or p == 2: return 1
    return fibonacci_recursivo(p-1) + fibonacci_recursivo(p-2)
    
# main
def main():
    p = int(input("Informe a posição: "))
    if p <= 0:
        print("Não pode - int e positiv")
    else:
        print(f"Valor na posição {p} = {fibonacci_recursivo(p)}")

if __name__ == "__main__":
    main()
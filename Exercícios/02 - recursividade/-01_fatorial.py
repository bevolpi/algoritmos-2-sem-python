# função recursiva para calcular o fatorial de um nm int e positivo
def fatorial(n: int) -> int:
    #caso base
    if n == 0: return 1
    return n * fatorial(n - 1)

''' n == 5 -> return 5 * a função dnv mas com o n == 4 e repete! pq nao tem ainda o resultado do caso base'''

# função principal - main
def main():
    n = int(input("Informe um valor int e positivo: "))
    if n < 0:
        print("Não pode - int positv")
    else: 
        print(f"{n}! = {fatorial(n)}")
        
# programa principal
if __name__ == "__main__":
    main()
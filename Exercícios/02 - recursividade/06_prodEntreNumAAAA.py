'''Defina uma função recursiva que recebe dois números naturais m e n e retorna
o produto de todos os números no intervalo [m, n]: m x (m – 1) x ... x (n – 1) x n 
-> é um fatorial que para num limite tipo: f(5,3) = 5 * 4 * 3 <-'''

def produto(m: int, n:int) -> int:
    if m < n: return produto(n, m)
    if m == n: return n
    return m * produto(m-1, n)

# e se for negativo??
def main():
    m = int(input("m = "))
    n = int(input("n = "))
    if n <= 0:
        print("nao pode")
    else:
        print(f"produtos entre {m} e {n} = {produto(m,n)}")
    
if __name__ == "__main__":
    main()
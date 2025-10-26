# função para verificar se um nm eh primo
def eh_primo(valor: int) -> bool:
    
# função p gerar n nms primos
def gerar_primos(n: int) -> list:
    lista = []
    valor = 2
    while len(lista) < n:
        if eh_primo(valor):
            lista.append(valor)
        valor += 1
    return lista
    
# função main
def main() -> None:
    n = int(input("Informe qtde de nms primos: "))
    lista = gerar_primos(n)
    imprimir(lista)
    
# programa principal
if __name__ == "__main__":
    main()
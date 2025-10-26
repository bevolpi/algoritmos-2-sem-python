#soma doselementos de um vetor
def soma(vetor, nm_elementos_vetor):
    if nm_elementos_vetor == 1: return vetor[0]
    else:
        return vetor[nm_elementos_vetor - 1] + soma(vetor, nm_elementos_vetor - 1)
    #return vetor[3-1] + soma([2,3,1], 3-1) -> vetor[2] + soma([2,3,1], 2)
    #return vetor[2-1] + soma([2,3,1], 2-1) -> vetor[1] + soma([2,3,1], 1) -> É 1 ENT RETORNE O vetor[0] =  2 e volte p cima
    
def main():
    vetor = [2,3,1]
    nm_elementos_vetor = len(vetor)
    print(f"soma dos elementos = {soma(vetor,nm_elementos_vetor)}")
    
if __name__ == "__main__":
    main()
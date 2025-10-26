'''Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas a partir do
terminal e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser
enforcado.
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!
Digite uma letra: O
A palavra é: _ _ _ _ O
Digite uma letra: E
A palavra é: _ E _ _ O
Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!'''

import random

#função para jogar
def jogar(palavras: str) -> str:
    escolher = random.choice(palavras).lower()
    #escolher = palavras[random.randint(0,len(palavras))]
    
    #listas auxiliares -> vetor é a msm coisa que lista
    linhas = ['_'] * len(escolher) 
    
    erro = 0
    while erro <= 6 and '_' in linhas:
        print(linhas)
        letra = input("Informe uma letra --> ")
        
        if letra in escolher:
            for i in range(len(escolher)):
                if escolher[i] == letra:
                    linhas[i] = letra
        else:
            erro += 1
            print(f"-> Você errou pela {erro}ª vez. Tente de novo!")
            
    if '_' not in linhas: 
        print("Você acertou!")
    else: 
        print("Enforcado!")
        
    
#funçao para ler e armazenar as palavras
def ler_palavras():
    palavras = []
    n_palavras = int(input("Quantas palavras? --> "))
    for i in range(n_palavras):
        palavras.append(input("Informe uma palavra --> "))
    return palavras

#função principal
def main():
    palavras = ler_palavras()
    jogar(palavras)

#programa principal
if __name__ == "__main__":
    main()


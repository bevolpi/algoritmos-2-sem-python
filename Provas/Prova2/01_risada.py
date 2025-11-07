def haha(palavra):
    palavra_vogais = ""
    for letra in palavra:
        if letra in "aeiou":
            palavra_vogais += letra

    if palavra_vogais == palavra_vogais[::-1]:
        return True
    else:
        return False

def main():
    palavra = input("Insira a risada: ").lower()

    if haha(palavra):
        print("sim")
    else:
        print("não")
        
if __name__ =='__main__':
    main()
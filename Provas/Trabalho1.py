# n =  int(input(""))

# for i in range (n):
#     a = input("")
#     frase = ""
#     for i in a:
#         if i.isalpha():
#             frase += chr(ord(i)+3)
#         else:
#             frase += i

#     frase = str(frase[::-1])
#     novafrase = ""

#     num = int(len(a)/2)
#     for i in range (len(a)):
#         if(i>=int(num)):
#             novafrase += chr(ord(frase[i])-1)
#         else:
#             novafrase += frase[i]
#     print(novafrase)
    
def passadas():
    n = int(input("Quantas códigos serão passados? "))
    
    for i in range(1, n+1):
        palavra = input(f"Escreva a palavra {i}: ")
        palavra_codificada = ""
        
        #1
        for letra in palavra:
            if letra.isalpha:
                palavra_codificada += chr(ord(letra) + 3) # só pq o .append nao funciona em string, ent o += é como se fosse um .append, mas em uma string
            else:
                palavra_codificada += letra
        
        #2
        palavra_invertida = palavra_codificada[::-1]
        
        #3
        metade = len(palavra_invertida) // 2
        resultado = ''
        
        for i in range(len(metade)):
            if i < metade:
                resultado += palavra_invertida[i]
            else: 
                resultado += chr(ord(palavra_invertida[i])-1)
        
        print(resultado)
        
def main():
    passadas()
    
if __name__ == '__main__':
    main()
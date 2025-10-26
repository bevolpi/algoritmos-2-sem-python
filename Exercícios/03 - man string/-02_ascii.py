'''print o cód correspondente da letra'''
ba = input("Informe uma palavra: ").lower() #só pode minúscula

# for letra in ba:
#     print(f"letra = {letra} | código = {ord(letra)}")
    
for i in range(len(ba)):
    print(f"letra = {ba[i]} | código = {ord(ba[i])}")


'''print o caractere correspondente do número'''
lista = [47, 69, 97, 124]
for i in lista:
    #print(str(i)) #virou uma string ent não dá p fazer conta
    print(chr(i)) #exibe o caractere especial correspondente
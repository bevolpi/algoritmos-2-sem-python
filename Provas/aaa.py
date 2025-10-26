#1
a =  int(input(""))
passada1 = []

for i in a:
    for i in a:
        if i.isalpha():
            passada1.append(chr(ord(i) + 3))
        else:
            passada1.append(i)
#2
    frase = str(frase[::-1])
    
#3
    novafrase = ""

    for i in frase:
        if(i>=int(len(a)/2)):
            aux = ord(frase[i])-1
        else:
            aux = ord(frase[i])
        novafrase = novafrase + chr(aux)
    print(novafrase)
t = tuple('python')
print(t)
print(t[0])
print(t[1:3])
#--------
t = tuple('python')
t = ('A',) + t[1:]
print(t)
#--------
t = (4, 5, 6)
a, b, c = t
print(a) # Saída: 4
print(b) # Saída: 5
print(c) # Saída: 6
#---------
t = (1, 2, 3, 4, 5)
a, *b, c = t
print(a) # Saída: 1
print(b) # Saída: [2, 3, 4]
print(c) # Saída: 5
# ---------
x = 10
y = 20
x, y = y, x
print(x) # Saída: 20
print(y) # Saída: 10

def processar(*args, **kwargs):
    print("Posicionais:", args)
    print("Nomeados:", kwargs)
    # Chamando com múltiplos argumentos
processar(nome="João", idade=25, cargo="x")
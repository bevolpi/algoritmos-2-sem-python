from ponto import Ponto

lista = list()

qtde = int(input("Qtde de pontos: "))

for _ in range(qtde):
    x = int(input("X = "))
    y = int(input("Y = "))
    lista.append(Ponto(x, y))

print('Distância de cada ponto até a origem (0,0):')
for pontinho in lista:
    print(f"{pontinho} --> {pontinho.calcular_dist_origem()}")
    
print()
print(f"Distância entre os pontos 1 e 2:")
print(round(lista[0].calcular_dist(lista[1])))
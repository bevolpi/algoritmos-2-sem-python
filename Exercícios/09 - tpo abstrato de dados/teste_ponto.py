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

#dá p achar a distancia com a origem assim tbm!
# for pontinho in lista:
#     d = pontinho.calcular_dist(Ponto(0,0))
#     print(f'Distancia entre o ponto e a origem: {d:.2f}')
    
print()
print(f"Distância entre os pontos 1 e 2:")
print(round(lista[0].calcular_dist(lista[1])))
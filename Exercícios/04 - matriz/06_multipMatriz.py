'''Uma empresa de vendas conta com 5 vendedores em seu quadro de funcionários. Esses
vendedores são responsáveis por divulgar e vender os produtos da empresa para
comerciantes da região. Foi solicitado a você que implementasse um programa em
Python para emitir alguns relatórios (impressão no vídeo) sobre as vendas realizadas no
primeiro semestre. Inicialmente o seu programa deverá armazenar o nome de cada um
dos vendedores e também o valor total das vendas de cada vendedor em cada mês do
primeiro semestre. O seu programa deverá imprimir no vídeo as seguintes informações:
a) Total de vendas de cada vendedor no primeiro semestre.
b) Total de vendas por mês.
c) Nome do vendedor que teve o maior total de vendas.
d) Nome do vendedor com o menor total de vendas'''

# para multiplicar as matrizes, é preciso:
#     M3x2 e N2X3 -> ou seja o 1 nm pode ser qualquer um, o 2 e o 3 precisam ser iguais e o 4 pode ser qualquer um -> pode ser M4X3 e N4X78, mas não M3X2 e N3X4
# M3x2 * N2x3 = P3x3 
# ((M[0][0] * N[0][0]) + (M[0][1] * N[1][0])) = P[0][0] 
# ((M[0][0] * N[0][1]) + (M[0][1] * N[1][1])) = P[0][1]
# ((M[0][0] * N[0][2]) + (M[0][1] * N[1][2])) = P[0][2] 

from random import randint

def ler_dados(matriz):
    matriz = [[randint(1, 5)for j in range(len(matriz))] for i in range(len(matriz))]
    
def imprimir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= "\t")
        print()

def multiplicar(a, b):
    # i == linhas do A
    # j == colunas do B
    # k == colunas de A e linhas de B
    c = []
    for i in range(len(a)):
        linha = []
        for j in range(len(b[0])):
            aux = 0
            for k in range(len(a[i])):
                aux += a[i][k] * b[k][j]
            linha.append(aux)
        c.append(linha) 
    return c

def main():
    a = [[1, 2], [3,0], [2,1]]
    b =[[1,0,1], [2,1,3]]
    imprimir(a)
    print()
    imprimir(b)
    c = multiplicar(a,b)
    print()
    imprimir(c)

if __name__ == '__main__':
    main()

'''Implemente uma função em Python para comparar as notas de alguns alunos na primeira prova e na segunda prova aplicada por um professor. A função deve receber como parâmetro duas listas de tuplas, onde cada tupla contém o nome de um aluno e sua nota em uma prova. A função deve exibir os seguintes resultados:
a) Alunos que melhoraram suas notas da primeira prova para a segunda.
b) Alunos que pioraram suas notas.
c) Alunos que mantiveram a mesma nota'''

def gerar_notas():
    p1 = list()
    p2 = list()
    for i in range(1, 3):
        nome = input(f"Nome aluno {i}: ")
        nota = int(input("Nota: "))
        p1.append((nome, nota))
    for i in range(1, 3):
        nome = input(f"Nome aluno {i}: ")

        nota = int(input("Nota: "))
        p2.append((nome, nota))
    return p1,p2

def comparar(p1, p2):
    nome, nota1 = zip(*p1)
    nome, nota2 = zip(*p2)
    comparada = []
    for i in range(len(nome)):
        if nota1[i] < nota2[i]:
            comparada.append(f"Notas {nome[i]}: {nota1[i]}, {nota2[i]} --> melhorou")
        elif nota2[i] < nota1[i]:
            comparada.append(f"Notas {nome[i]}: {nota1[i]}, {nota2[i]} --> piorou")
        else:
            comparada.append(f"Notas {nome[i]}: {nota1[i]}, {nota2[i]} --> manteve")
    return comparada
    
def main():
    p1, p2 = gerar_notas()
    print(f"Prova 1: {p1}")
    print(f"Prova 2: {p2}")
    
    comparada = comparar(p1,p2)
    for i in range(len(comparada)):
        print(comparada[i])
    
    
if __name__ == '__main__':
    main()


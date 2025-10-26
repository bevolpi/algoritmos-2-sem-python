'''Programa exemplo para ler o RA, Nome e a Nota dos alunos matriculados em Felicidade. Em seguida, imprimir a quantidade de alunos com média maior ou igual a 7'''

lista = []

for i in range(2):
    ra = int(input("RA: "))
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    lista.append({'ra' : ra,'nome' : nome, 'nota' : nota })    
    print()

#  qtde de alunos com nota acima da média
total = 0
for i in range(len(lista)):
    aluno = lista[i] # aluno é o dict inteiro
    if aluno["nota"] >= 7:
        total += 1
        
# SEGUNDA MANEIRA! -> melhor  
total = 0
for aluno in lista:
    if aluno.get('nota') >= 7:
        total += 1
    

print(lista)
print(f"{total} alunos estão acima da média")
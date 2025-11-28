from aluno import Aluno

# lista de alunos
x = list() #essa list é um construtor
x = dict()
x = Aluno() #....

lista = []
for _ in range(3):
    nome = input('Nome --> ')
    ra = int(input('RA --> '))
    nota1 = float(input('Nota 1 --> '))
    nota2 = float(input('Nota 2 --> '))
    
    lista.append(Aluno(nome, ra, nota1, nota2)) 
    
    print('-' * 30)
    
# impressão do nome, da média e da situação
print(f'{'Nome':<20}{'Média':<10}{'Situação'}') #coluna com espaçamento de 20 caracteres (se nao entrar nenhum valor, ela fica vazia)
print('-' * 40)

for aluninho in lista:
    media = aluninho.calcular_media()
    print(f'{aluninho.nome:<20}{media:<10.2f}{aluninho.situacao()}')
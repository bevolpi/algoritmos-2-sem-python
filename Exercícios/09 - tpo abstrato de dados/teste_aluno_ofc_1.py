'''Codifique um Tipo Abstrato de Dados (TAD) chamado Aluno contendo os seguintes
atributos (propriedades): RA, nome, nota1 e nota2. A classe deve apresentar o
método construtor e também os métodos para calcular e retornar a média
aritmética do aluno e retornar a situação do aluno (aprovado ou reprovado).
Em seguida, gere alguns objetos do tipo Aluno e faça a inserção em uma lista. Após a
geração dos objetos, imprima o nome do aluno, sua média e sua situação.
Codifique um Tipo Abstrato de Dados (TAD) chamado Aluno contendo os seguintes
atributos (propriedades): RA, nome, nota1 e nota2. A classe deve apresentar o
método construtor e também os métodos para calcular e retornar a média
aritmética do aluno e retornar a situação do aluno (aprovado ou reprovado).
Em seguida, gere alguns objetos do tipo Aluno e faça a inserção em uma lista. Após a
geração dos objetos, imprima o nome do aluno, sua média e sua situação.'''

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
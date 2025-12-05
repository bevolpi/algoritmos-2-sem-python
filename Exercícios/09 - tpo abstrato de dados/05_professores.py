'''Calcule o salário bruto:
1. Salário base
    basta multiplicar o número de aulas semanais por 4,5 semanas e pelo valor da hora-aula. Se título de mestre = 8,5% --> título de doutor = aumento será de 12%, no valor do salário base.
2. Adicional de hora-atividade
    Hora extra: adicional de 5%, aplicado sobre o salário base.
3. Descanso Semanal Remunerado
    Corresponde a 1/6 sobre a remuneração total
Desenvolva um programa em python que gere três objetos representando os professores e, em seguida, imprima no vídeo o valor do salário bruto de cada professor. A entrada dos dados para cada professor deverá ser realizada via teclado.'''

from professor import Professor

lista = []
for _ in range(3):
    nome = input('Nome --> ')
    nm_aulas_semanais = int(input('Números de Aulas Semanais --> '))
    vlr_hr_aula = float(input('Valor Hora-Aula --> '))
    titulo = input('Título (mestre, doutor, nenhum) --> ')
    hora_extra = input("Fez hora extra? --> ")

    lista.append(Professor(nome, nm_aulas_semanais, vlr_hr_aula, titulo, hora_extra)) 
    
    print('-' * 30)
    
print(f'{'Nome':<20}{'Salário Bruto'}') 
print('-' * 40)

for professor in lista:
    salario_bruto = professor.calcular_sal_bruto()
    print(f'{professor.nome:<20}{salario_bruto}')
'''arquivo texto (o que conseguimos ler) e 
arquivo binário (não lemos, somente símbolos)'''

#bloco de leitura  de arquivo
#com o "alunos" aberto em forma de leitura (read="r"), chame ele de arquivo (pode ser qualquer nome ao invés de arquivo)

total = 0

with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip() #p tirar os espaços sobrando no final das frases
        nome, nota1, nota2 = linha.split(";") 
        # desacopla as infos de acordo com ";": nome=Ana Aparecida nota1=10 nota2=8
        media = (float(nota1)+float(nota2))/2
        if media >= 7:
            print(F"Aluno {nome} foi aprovado!--> Com média {media:.1f}")
            total += 1
        else: 
            print(f'Aluno {nome} foi reprovado!--> Com média {media:.1f}')
print(f"Total de alunos aprovados {total:.0f}")

#obs: qnd quero converter o tipo da variavel - isso se chama "cast"
# em outras linguagens = (float)x --> em python = float(x)
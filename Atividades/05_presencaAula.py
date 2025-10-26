'''Você foi designado para desenvolver um pequeno sistema que analisa as presenças dos alunos em um curso. As aulas realizadas estão registradas em uma lista, e as presenças de cada aluno estão armazenadas em um dicionário, onde cada valor é uma lista de marcações na mesma ordem das aulas. Cada marcação pode ser: "P" → Presente e "F" → Falta
O sistema deve calcular indicadores individuais e da turma. Considerar as variáveis a seguir que poderão ter qualquer quantidade de elementos
aulas = ["A1", "A2", "A3", "A4", "A5"]
presencas = {
"Ana": ["P", "P", "F", "P", "P"],
"Bruno": ["P", "F", "F", "P", "F"],
"Carla": ["P", "P", "P", "P", "P"],
"Diego": ["F", "F", "P", "F", "P"]
}
Escreva um programa em Python que realize as seguintes funcionalidades:
a) Para cada aluno, calcule:
 total de presenças (P);
 total de faltas (F);
 percentual de presença (% de aulas assistidas).
b) Gere um dicionário por_aluno com as informações no formato: "Ana": {"P": 4, "F": 1, "perc": 80.0, "situacao": "APROVADO"}. O aluno é considerado APROVADO se sua presença for ≥ 75%.
c) Calcule e exiba:
 a aula com mais faltas (ex: "A2");
 o aluno com maior presença;
 o aluno com mais faltas;
 a média de presença da turma (em %).
d) O relatório final deve seguir o formato:
relatorio = {
"por_aluno": {...},
"aula_mais_faltas": "...",
"melhor_presenca": "...",
"mais_faltas": "...",
"presenca_media_turma": ...}'''

# a) qtde de presenças e faltas
def qtde_presenca(presencas):
    p = {}
    f = {}
    for nome in presencas:
        p[nome] = 0
        f[nome] = 0
    for nome, anotacoes in presencas.items():
        for anotacao in anotacoes:
            if anotacao == "P":
                p[nome] += 1
            else:
                f[nome] += 1
    return p, f
        
# percentual de presenças 
def percentual_presencas(p,aulas):
    percentual = {}
    for nome, presenca in p.items():
        calculo = (presenca / len(aulas)) * 100
        
        if nome not in percentual:
            percentual[nome] = calculo
    return percentual 
                   
# b) por_aluno = "Ana": {"P": 4, "F": 1, "perc": 80.0, "situacao": "APROVADO"}. --> APROVADO se sua presença for ≥ 75%.

def registro_aprovacao(p, f, percentual):
    por_aluno = {} 
    for nome in p:
        pres = p[nome] #pres recebe o valor atribuído ao primeiro aluno (Ana)
        falt = f[nome]
        perc = percentual.get(nome) #ambas as maneiras de indicar funcionam
        if perc >= 75:
            situ = "APROVADO"
        else:
            situ = "REPROVADO"
            
        por_aluno[nome]  = {"P": pres, "F": falt, "perc": perc, "situacao": situ}
    return por_aluno

# c) a aula com mais faltas (ex: "A2");

def aula_falta(aulas, presencas):
    registro = {}
    for aula in aulas:
        registro[aula] = 0 # o dicionário com 0 faltas para cada aula

    for i in range(len(aulas)):
        aula = aulas[i]
        for presenca in presencas.values():
            if presenca[i] == "F":
                registro[aula] += 1
    maior = 0
    maior_nome = ''
    for aula,qtde in registro.items():
        if qtde > maior:
            maior = qtde
            maior_nome = aula
            
    return maior_nome

# o aluno com maior presença; o aluno com mais faltas;
def presenca_aluno(p, f):
    # aluno com maior presença
    maior_presenca_qtde = -1  
    mais_p = ""              
    for aluno, qtde in p.items():
        if qtde > maior_presenca_qtde:
            maior_presenca_qtde = qtde
            mais_p = aluno
    
    #aluno com mais faltas
    maior_falta_qtde = -1 
    mais_f = ""           
    for aluno, qtde in f.items():
        if qtde > maior_falta_qtde:
            maior_falta_qtde = qtde
            mais_f = aluno
            
    return mais_p, mais_f

# a média de presença da turma (em %).
def media(aulas, p):
    soma = 0
    geral = 0
    for presenca in p.values():
        soma += presenca 
        geral += presenca * len(aulas)
    total = (soma/geral) * 100
    return total

def media(aulas, p):
    total_presencas_turma = sum(p.values())
    total_aulas = len(aulas)
    num_alunos = len(p)
    
    total_aulas_turma = total_aulas * num_alunos 
    
    if total_aulas_turma > 0:
        media_perc = (total_presencas_turma / total_aulas_turma) * 100
        return media_perc
    else:
        return 0.0

def main():
    aulas = ["A1", "A2", "A3", "A4", "A5"]
    presencas = {
        "Ana": ["P", "P", "F", "P", "P"],
        "Bruno": ["P", "F", "F", "P", "F"],
        "Carla": ["P", "P", "P", "P", "P"],
        "Diego": ["F", "F", "P", "F", "P"]
    }
    p, f = qtde_presenca(presencas)
    # print(f"Qtde total de presenças: {p}")
    # print(f"Qtde total de faltas: {f}")
    
    percentual = percentual_presencas(p, aulas)
    # print(f"% de aulas assistidas: {percentual}")
    
    por_aluno = registro_aprovacao(p, f, percentual)
    # print(f"Registro por aluno: {por_aluno}")
    
    aula_mais_faltas = aula_falta(aulas, presencas)
    # print(f"Aula com mais faltas: {aula_mais_faltas}")
    
    mais_p,  mais_f = presenca_aluno(p,f)
    # print(f"Aluno(s) com mais presenças: {mais_p}")
    # print(f"Aluno(s) com mais faltas: {mais_f}")
    
    total_media = media(aulas, p)
    # print(f"Média de presença da sala: {total_media}%")
    
    relatorio = {
        "por_aluno": por_aluno,
        "aula_mais_faltas": aula_mais_faltas,
        "melhor_presenca": mais_p,
        "mais_faltas": mais_f,
        "presenca_media_turma": total_media
        }
    
    print(relatorio)
    
if __name__ == '__main__':
    main()
'''A equipe de marketing de uma agência roda campanhas em vários canais (Instagram, Google Ads, Indicação etc.) e registra tudo no CRM. A exportação do CRM traz uma lista de leads, cada um com:
 origem (canal de captação),  score (qualidade/interesse de 0 a 100),  status ("ganho" quando virou cliente; "perdido" caso contrário).
    leads = [{"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},...]
O gerente solicitou a você três tarefas:
a) Filtrar apenas os leads qualificados (score ≥ 70).
b) Calcular a taxa de conversão por origem:
taxa origem = nº de ganhos na origem/nº total de leads na origem -> considerando convertido quando status ==
"ganho".
'''

lista = []
# total = int(input("Qual o total de leads? "))

# for i in range(total):
#     nome = input("Nome: ")
#     origem = input("Origem: ")
#     score = int(input("score: "))
#     status = input("Status: ")
#     lista.append({'nome' : nome, 'origem': origem, 'score': score, 'status':
#     status})    
#     print()

lista = [
        {"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},
        {"nome":"Beto","origem":"Google Ads","score":65,"status":"perdido"},
        {"nome":"Cris","origem":"Indicação","score":90,"status":"ganho"},
        {"nome":"Duda","origem":"Instagram","score":74,"status":"perdido"},
        {"nome":"Enzo","origem":"Google Ads","score":71,"status":"ganho"},
    ]
# a) Filtrar apenas os leads qualificados (score ≥ 70).
print('Leads qualificados:')
for lead in lista:
    if lead["score"] >= 70:
        score = lead.get('nome')
        print(score)

# b) Calcular a taxa de conversão por origem:
    #nº de ganhos na origem
ganhosOrigem = {}
for lead in lista:
    if lead['status'] == 'ganho':
        if lead['origem'] in ganhosOrigem:
            ganhosOrigem[lead['origem']] += 1
        else:
            ganhosOrigem[lead['origem']] = 1
            
    #nº total de leads na origem
ttOrigem = {}
for lead in lista:
    if lead['origem'] in ttOrigem:
        ttOrigem[lead['origem']] += 1
    else:
        ttOrigem[lead['origem']] = 1

# taxaFinal = {}
# for i in range(total):
#     taxaFinal[i] = (ganhosOrigem[i]/ttOrigem[i])--->>> ERRADOOO!!
taxaFinal = {}
for origem in ttOrigem:
    taxaFinal[origem] = (ganhosOrigem.get(origem, 0) / ttOrigem[origem]) * 100
    #(origem, 0) -> é p pegar o valor da origem e se nao existir, retorna 0

print()
print('Taxa conversão:')
for origem, taxa in taxaFinal.items():
    print(f"{origem} -> {taxa}%")
'''A equipe de marketing de uma agência roda campanhas em vários canais (Instagram, Google Ads, Indicação etc.) e registra tudo no CRM. A exportação do CRM traz uma lista de leads, cada um com:
 origem (canal de captação),  score (qualidade/interesse de 0 a 100),  status ("ganho" quando virou cliente; "perdido" caso contrário).
    leads = [{"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},...]
O gerente solicitou a você três tarefas:
a) Filtrar apenas os leads qualificados (score ≥ 70).
b) Calcular a taxa de conversão por origem:
taxa origem = nº de ganhos na origem/nº total de leads na origem -> considerando convertido quando status ==
"ganho".
'''

def filtrar(leads: list[dict]):
    qualificados = []
    for lead in leads: 
        if lead.get('score') >= 70:
            qualificados.append(lead)
            print(lead.get('nome'))

def taxa_conversao(leads: list[dict]):
    totais : dict[str, int] = {} #-> p mostrar qq o dict vai receber
    ganho : dict[str, int] = {}
    
    for lead in leads:
        origem = lead.get('origem')
        status = lead.get('status')
        
        if origem not in totais:
            totais[origem] = 0
            ganho[origem] = 0
            
        totais[origem] += 1
        if status == 'ganho':
            ganho[origem] += 1
            
    #cálculo da tx de conversão
    for origem in totais:
        t = totais.get(origem)
        g = ganho.get(origem)
        taxa = g/t if t > 0 else 0
        # eu divido só se t é maior q 0, se não já joga 0
        print(f"{origem} --> {(taxa*100):.2f}%")

def main():
    leads = [
        {"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},
        {"nome":"Beto","origem":"Google Ads","score":65,"status":"perdido"},
        {"nome":"Cris","origem":"Indicação","score":90,"status":"ganho"},
        {"nome":"Duda","origem":"Instagram","score":74,"status":"perdido"},
        {"nome":"Enzo","origem":"Google Ads","score":71,"status":"ganho"},
    ]
    
    filtrar(leads)
    taxa_conversao(leads)
if __name__ == '__main__':
    main()
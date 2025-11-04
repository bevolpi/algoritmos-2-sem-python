'''Uma empresa coleta, ao fim de cada atendimento, a nota de satisfação do cliente (0 a 10) e o canal utilizado: aplicativo, loja física, telefone, site, etc. O gestor quer um relatório simples para entender a qualidade de cada canal e identificar atendimentos muito bons (≥ 9) ou críticos (≤ 4). Você recebeu uma lista de respostas, onde cada resposta é um dicionário com:
 canal (str): nome do canal de atendimento
 nota (float ou int): nota de satisfação (0-10)
Seu objetivo é produzir métricas por canal e filtrar respostas por um limiar.
a) Calcular a média por canal.
b) Calcular a contagem de por canal.'''
# ENTENDER O PQ QUE TA ERRADO OS DO COMENTÁRIOOSSSSSSSSSSSS


# def media(respostas):
#     mediaCanal = {}
#     soma = 0
#     for resp in respostas:
#         ocorrencia = 0
#         if resp ["canal"] not in mediaCanal:
#             mediaCanal["canal"] = resp["canal"]
#             mediaCanal["soma"] = resp["nota"]
#             ocorrencia = 1
#         else:
#             mediaCanal["soma"] += resp["nota"]
#             ocorrencia += 1
#         mediaCanal["media"] = mediaCanal["soma"] / ocorrencia


#     del mediaCanal["soma"]
#     return mediaCanal

def media(respostas):
    soma_cont = {}
    for resp in respostas:
        canal = resp['canal']
        nota = resp['nota']
        if canal not in soma_cont:
            soma_cont[canal] = {'soma': nota, 'cont': 1}
        else:
            soma_cont[canal]['soma'] += nota
            soma_cont[canal]['cont'] += 1
    # retornar média por canal
    mediaCanal = {}
    for canal, d in soma_cont.items():
        mediaCanal[canal] = d['soma'] / d['cont']
    return mediaCanal
            
def classificar(respostas):
    # aqui conta quantas respostas há por canal
    contagem = {}
    for resp in respostas:
        canal = resp['canal']
        contagem[canal] = contagem.get(canal, 0) + 1
    return contagem
# ...existing code...
# def classificar(respostas):
#     classificacao = {}
#     for resp in respostas:
#         if resp["canal"] not in classificacao:
#             classificacao["canal"] = resp.get("canal")
#             classificacao["nota"] = resp.get("nota")
#         else:
#             classificacao["nota"] += resp.get("nota")
#     return classificacao

def main():
    respostas = [
        {"canal": "Aplicativo", "nota": 9.5},
        {"canal": "Loja Física", "nota": 8},
        {"canal": "Telefone", "nota": 4},
        {"canal": "Site", "nota": 6.5},
        {"canal": "Aplicativo", "nota": 10},
        {"canal": "Telefone", "nota": 3},
        {"canal": "Loja Física", "nota": 9},
        {"canal": "Site", "nota": 2.5}
    ]
    
    mediaCanal = media(respostas)
    print(mediaCanal)
    
    classificacao = classificar(respostas)
    print(classificacao) 
       
if __name__ == '__main__':
    main()
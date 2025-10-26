'''Uma pequena mercearia utiliza um sistema simples para registrar suas vendas diárias. Os preços de cada produto estão armazenados em um dicionário, e cada venda é representada por uma lista de itens vendidos. O gerente deseja obter algumas informações consolidadas para analisar o desempenho das vendas do dia. Observação: você deve considerar as variáveis com os nomes precos e vendas.
Você deverá escrever um Python que execute as seguintes funcionalidades:
a) Calcule o total de cada venda e armazene os resultados em uma lista chamada totais_venda.
b) Calcule o faturamento total (soma de todas as vendas).
c) Gere um dicionário qtd_por_item com a quantidade total vendida de cada produto.
d) Identifique: o produto mais vendido (maior quantidade); E o produto com maior faturamento individual (quantidade x preço).
e) Calcule o ticket médio da loja (faturamento total ÷ número de vendas).
f) Organize as informações em um dicionário relatorio com o formato:
relatorio = {
"totais_venda": [...],
"faturamento_total": ...,
"qtd_por_item": {...},
"mais_vendido": "...",
"mais_faturado": "...",
"ticket_medio": ...
}'''

#a) total de cada venda
def preco_cada(vendas, precos):
    totais_venda = []
    for venda in vendas:
        soma = 0
        for produto in venda:
            for nome, preco in precos.items():
                if nome == produto:
                    soma += preco
        totais_venda.append(f"R$ {soma:.2f}")
    return totais_venda

# b) faturamento total
def preco_total(vendas, precos):
    soma_geral = 0
    for venda in vendas:
        soma = 0
        for produto in venda:
            for nome, preco in precos.items():
                if nome == produto:
                    soma += preco
        soma_geral += soma
    return round(soma_geral, 2)

# c) Quantidade total vendida de cada produto.
def qtde_total(vendas):
    qtde_por_item = {}
    for venda in vendas:
        for produto in venda:
            if produto in qtde_por_item:
                qtde_por_item[produto] += 1
            else:
                qtde_por_item[produto] = 1
    return qtde_por_item

# d) produto mais vendido (maior quantidade);
def mais_vendido(qtde_por_item):
    maior = 0
    maior_nome = ''
    for nome,qtde in qtde_por_item.items():
        if qtde > maior:
            maior = qtde
            maior_nome = nome
    return maior_nome

# produto com maior faturamento individual (quantidade × preço).
def maior_faturamento(qtde_por_item, precos):
    faturamento = {}
    maior = 0
    maior_nome = ""
    for nome, preco in precos.items():
        for produto, qtde in qtde_por_item.items():
            if nome == produto:
                faturamento[nome] = qtde * preco
                
    for nome_i, faturamento_i in faturamento.items():
        if faturamento_i > maior:
            maior = faturamento_i
            maior_nome = nome_i
    return maior_nome
            
# e) ticket médio = (faturamento total ÷ número de vendas).
# def ticket_medio(preco_geral, qtde_por_item):
#     qtde_tt = 0
#     for qtde in qtde_por_item.values():
#         qtde_tt += qtde
#     ticket = preco_geral / qtde_tt
#     return ticket  --> está errado, aqui estamos fazendo faturamento total /  qtde total de produtos vendidos

def ticket_medio(preco_geral, vendas):
    ticket = preco_geral / len(vendas)
    return round(ticket, 2)
                      
            

def main():
    precos = {
        "arroz": 22.5,
        "feijao": 9.8,
        "leite": 4.7,
        "pao": 1.5
        }
    vendas = [
        ["arroz", "feijao", "feijao", "leite"],
        ["pao", "pao", "pao", "leite"],
        ["arroz", "leite"],
        ["feijao", "feijao", "feijao"]
    ]
    
    totais_venda = preco_cada(vendas, precos)
    # print(f"Preço de cada venda: R$ {totais_venda}")
    
    preco_geral = preco_total(vendas,  precos)
    # print(f"Preço total das vendas: R$ {preco_geral:.2f}")
    
    qtde_por_item = qtde_total(vendas)
    # print(f"Quantidade vendida por item: {qtde_por_item}")
    
    maior_vendido = mais_vendido(qtde_por_item)
    # print(f"Produto mais vendido: {maior_vendido}")
    
    maior_valor = maior_faturamento(qtde_por_item, precos)
    # print(f"Produto com maior faturamento individual: {maior_valor}")
    
    ticket = ticket_medio(preco_geral, qtde_por_item)
    # print(f"Ticket médio da loja: R$ {ticket:.2f}")

# f) infos organizadas  
    relatorio = {
        "totais_venda": totais_venda,
        "faturamento_total": preco_geral,
        "qtd_por_item": qtde_por_item,
        "mais_vendido": maior_vendido,
        "mais_faturado": maior_valor,
        "ticket_medio": ticket
    }
    
    print(relatorio)
    
if __name__ == '__main__':
    main()
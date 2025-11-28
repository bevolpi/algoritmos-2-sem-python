def gasto_pedido(dici):
    totais = {}
    for pedido, info in dici.items():
        produtos = info["produtos"]
        valor = sum(produtos.values())
        totais[pedido] = valor
    return totais

def gasto_cliente(dici):
    totais = {}
    for info in dici.values():
        cliente = info["cliente"]
        valor = sum(info["produtos"].values())
        
        if cliente in totais:
            totais[cliente] += valor
        else:
            totais[cliente] = valor
            
    return totais

def maior_gasto(dici):
    maior = 0
    cliente_maior = ""
    for cliente, valor in dici.items():
        if valor > maior:
            maior = valor
            cliente_maior = cliente
    return cliente_maior
    
        
def faturamento(dici):
    soma = sum(dici.values())
    return soma
    
def main():
    pedidos = {
        "P001": {"cliente": "Ana", "produtos": {"Mouse": 80.0, "Teclado": 120.0}},
        "P002": {"cliente": "Bruno", "produtos": {"Monitor": 700.0}},
        "P003": {"cliente": "Ana", "produtos": {"Cabo HDMI": 40.0, "Mouse": 80.0}},
        "P004": {"cliente": "Carla", "produtos": {"Cadeira Gamer": 950.0}}
        }
    
    print(gasto_pedido(pedidos))
    por_cliente = gasto_cliente(pedidos)
    print(por_cliente)
    
    cliente_mais_gastou = maior_gasto(por_cliente)
    print(f"o cliente com maior gasto foi {cliente_mais_gastou}")
    
    faturamento_total = faturamento(por_cliente)
    print(f"o faturamento foi de R${faturamento_total:.2f}")
    
if __name__ == "__main__":
    main()

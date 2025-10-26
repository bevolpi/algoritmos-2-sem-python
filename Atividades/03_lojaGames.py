'''Uma loja online registra os pedidos de seus clientes em um dicionário, onde a chave é o ID
do pedido e o valor contém informações do cliente e dos produtos. Seu objetivo é gerar relatórios
de vendas e clientes usando apenas dicionários.
O dicionário contendo os pedidos deverá ter o nome pedidos e deverá ter a estrutura conforme
exemplo a seguir. Durante a avaliação serão utilizados outros exemplos, mas seguindo a mesma
estrutura.
pedidos = {
"P001": {"cliente": "Ana", "produtos": {"Mouse": 80.0, "Teclado": 120.0}},
"P002": {"cliente": "Bruno", "produtos": {"Monitor": 700.0}},
"P003": {"cliente": "Ana", "produtos": {"Cabo HDMI": 40.0, "Mouse": 80.0}},
"P004": {"cliente": "Carla", "produtos": {"Cadeira Gamer": 950.0}}
}
Escreva um programa em Python que realize as seguintes funcionalidades:
a) Calcular o total gasto em cada pedido. Exemplo: {"P001": 200.0, "P002": 700.0, ...}.
b) Calcular o total gasto por cliente. Exemplo: {"Ana": 320.0, "Bruno": 700.0, "Carla": 950.0}.
c) Identificar o cliente que mais gastou.
d) Calcular e imprimir o faturamento total da loja'''

# a) total gasto e cada pedido
def total_pedido(pedidos):
    for pedido, info in pedidos.items(): 
        soma = 0
        for preco in info["produtos"].values():
            soma += preco
        print(f"{pedido}: {soma}")
        
# b) total gasto por cliente.
def total_cliente(pedidos):
    tt_cliente = {}
    for info in pedidos.values(): 
        soma = 0
        cliente = info["cliente"]
        for preco in info["produtos"].values():
            soma += preco
        if cliente in tt_cliente:
            tt_cliente[cliente] += soma
        else:
            tt_cliente[cliente] = soma
    return tt_cliente

#c) cliente que mais gastou
def cliente_rico(tt_cliente):
    melhorCliente = ""
    maiorValor = -1
    for cliente, valor in tt_cliente.items():
        if valor > maiorValor:
            melhorCliente = cliente
    return melhorCliente

# d) faturamento total
def faturamento(tt_cliente):
    total = 0
    for valor in tt_cliente.values():
        total += valor
    return total
    
def main():
    pedidos = {
    "P001": {"cliente": "Ana", "produtos": {"Mouse": 80.0, "Teclado": 120.0}},
    "P002": {"cliente": "Bruno", "produtos": {"Monitor": 700.0}},
    "P003": {"cliente": "Ana", "produtos": {"Cabo HDMI": 40.0, "Mouse": 80.0}},
    "P004": {"cliente": "Carla", "produtos": {"Cadeira Gamer": 950.0}}
    }
    
    print("Soma total dos pedidos:")
    total_pedido(pedidos)
    
    print()
    
    print("Soma total por cliente: ")
    tt_cliente = total_cliente(pedidos)
    print(tt_cliente)
    
    print()
    
    print("Cliente que mais gastou: ")
    melhorCliente = cliente_rico(tt_cliente)
    print(melhorCliente)
    
    print()
    print("Faturamento total da loja: ")
    faturamentoTT = faturamento(tt_cliente)
    print(f"R$ {faturamentoTT:.2f}")
    

if __name__  == "__main__":
    main()
    

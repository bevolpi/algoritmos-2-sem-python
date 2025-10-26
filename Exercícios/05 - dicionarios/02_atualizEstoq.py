'''Uma mercearia de bairro mantém um cadastro enxuto dos produtos com três informações:
 saldo: quantidade atual em estoque;
 min: estoque mínimo desejado para não faltar produto;
 preco: preço unitário de reposição.
Durante o dia, o sistema registra movimentações: entradas positivas (reposição, devolução) e
saídas negativas (vendas, perdas). No fechamento, o gerente precisa:
a) aplicar as movimentações ao estoque;
b) listar quais produtos ficaram abaixo do mínimo, para facilitar o pedido de compra.'''

#função para atualizar estoque
def atualizar(estoque, movimentacao):
    for mov in movimentacao:
        produto = mov[0]
        qtde = mov[1]
        
        if produto not in estoque:
            estoque[produto] = {'saldo': qtde, 'min': 0, 'preco': 0}
            #atribui todos por 0
        
        estoque[produto]['saldo'] += qtde
'''FAZER ISSO AQUI Q TÁ ERRADO
def compra(estoque):
    for est in estoque:
        if estoque[produto]['saldo'] >= estoque[produto]['min']:
            print(estoque[produto])'''

def compra(estoque, produto):
    ...
def main():
    estoque = {
        "café": {"saldo": 10, "min": 12, "preco": 12.50},
        "pão": {"saldo": 30, "min": 25, "preco": 2.00},
        "queijo": {"saldo": 5, "min": 12, "preco": 34.00},
    }
    
    movimentacao = [
        ["café", -3],
        ["pão", -10],
        ["café", 5],
        ["leite", 8] # produto novo não cadastrado
    ]
    
    #atualizar o estoque a parir das movimentações diárias
    atualizar(estoque, movimentacao)
    produto = 0 #errado!
    compra(estoque, produto)

if __name__ == '__main__':
    main()
    
    
    
#---------------------------------------------------------------=


def Aplicar_Movimentacao(estoque: dict ,movimentacoes: list[list]) -> dict:
    
    for mov in movimentacoes:
        produto = mov[0]
        quantidade = mov[1]
        
        if produto not in estoque:
            estoque[produto] = {"saldo": quantidade, "min": 0, "preco": 0} 
        
        else:
            estoque[produto]["saldo"] += quantidade
    
def Mostrar_Produtos_AbaixoEstoque(estoque: dict) -> dict:
    
    produtosAbaixoEstoque = {}
    
    for produto in estoque:
        if estoque[produto].get('saldo') < estoque[produto].get("min"):
            produtosAbaixoEstoque[produto] = estoque[produto]
    
    return produtosAbaixoEstoque
                    
def main():    
    
    estoque = {
        "café": {"saldo": 10, "min": 12, "preco": 12.50},
        "pão": {"saldo": 30, "min": 25, "preco": 2.00},
        "queijo": {"saldo": 5, "min": 12, "preco": 34.00},
    }

    movimentacao = [
        ["café", -3],
        ["pão", -10],
        ["café", 5],
        ["leite", 8] # produto novo não cadastrado
    ]
    
    Aplicar_Movimentacao(estoque, movimentacao)
    
    # print(estoque)
    
    print(Mostrar_Produtos_AbaixoEstoque(estoque))
    
    
    
if __name__ == "__main__":
    main()
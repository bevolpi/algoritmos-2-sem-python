'''Implemente uma função em Python chamada cadastro() que receba um número variável de funcionários com seus respectivos dados (nome, idade,
cargo). Além disso, implemente uma função chamada atualizar() que receba um dicionário com as informações de um funcionário e atualize esses dados.
Utilizar os conceitos de gather e scatter.
Requisitos:
a) A função cadastro() deve uma quantidade variável de funcionários (tuplas) e
retornar uma lista de dicionários.
b) A função atualizar() deve aceitar um dicionário que representa um
funcionário e permita atualizar suas informações.
c) Exibir a lista de funcionários cadastrados ao final'''


def cadastro(*dados):
    lista = []
    for nome, idade, cargo in dados:
        lista.append({
            "nome": nome,
            "idade": idade,
            "cargo": cargo
        })
    return lista

def atualizar(funcionario, **novos_dados):
    for chave, valor in novos_dados.items():
        if chave in funcionario:
            funcionario[chave] = valor


# ======= Exemplo de uso =======
def main():
    funcionarios = cadastro(
        ("Ana", 29, "Analista"),
        ("Bruno", 35, "Gerente"),
        ("Carla", 22, "Estagiária")
    )

    print("Funcionários cadastrados inicialmente:")
    for f in funcionarios:
        print(f)

    # Atualizando funcionário (exemplo: Bruno mudou de cargo e idade)
    atualizar(funcionarios[1], idade=36, cargo="Coordenador")

    print("\nApós atualização:")
    for f in funcionarios:
        print(f)
        
if __name__ == '__main__':
    main()

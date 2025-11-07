def amplitude(dado):
    data, cmin, cmax = dado
    delta = cmax - cmin
    return delta

def indices_diarios(dados):
    indices = []
    for dado in dados:
        data, cmin, cmax = dado
        ampliando = amplitude(dado)
        media_conc = (cmin + cmax) / 2
        indice = (data, media_conc, ampliando)
        indices.append(indice)
    return indices

def pior_dia(indice_diarioa):
    maior = 0 
    data_maior = ""
    for indice in indice_diarioa:
        if indice[1] > maior:
            maior = indice[1]
            data_maior = indice[0]
    return data_maior

def main():
    n = int(input("Qtde de registros: "))
    dados = []

    for _ in range(n):
        data = input("Data: ")
        cmin = float(input("Conc_Min: "))
        cmax = float(input("Conc_Max: "))
        dados.append((data, cmin, cmax))

    for i in range(len(dados)):   
        print(f"Amplitude dia {dados[i][0]}: {amplitude(dados[i]):.2f}")

    indice_diarioa = indices_diarios(dados)
    print(f"Índices diários: {indice_diarioa}")

    print(f"Pior dia: {pior_dia(indice_diarioa)}")
    
if __name__ == '__main__':
    main()

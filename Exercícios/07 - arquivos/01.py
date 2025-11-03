from random import randint
n = 12
with open("financiamento.txt", "r", encoding="utf-8") as arquivo: #utf-8 p conseguir ver os acentos 
    financiamento = {}
    for linha in arquivo:
        linha = linha.strip()
        if linha == "":
            continue # se a linha estiver em branco, passa p próxima linha
        nome, pv = linha.split(";") 
        
        print()
        
        i = randint(1,4)/100
        pv = round(float(pv),2)
        pmt = round(float(pv) * ((i * (i + 1)**n) / (((i + 1)**n) - 1)),  2)
        
        financiamento["Nome"] = nome
        financiamento["Financiamento"] = float(pv)
        financiamento["Taxa Juros"] = i 
        financiamento["Valor Parcela"] = pmt
        
        print(financiamento)
        # print(f"{nome} pretende financiar R${float(pv):.2f} em {n} parcelas de {pmt:.2f}% de juros")
# selminininho, quando rodo pela primeira vez a compatibilidade não aparece em alguns casos
# normalmente na segunda dá certo :))))

def verificar(lista):
    for dicio in lista:
        if len(dicio["pai"]) != len(dicio["filho"]) or len(dicio["pai"]) < 2:
            print("SEQUÊNCIAS DE TAMANHO INVÁLIDO")
            return False
        
        meio = len(dicio["pai"]) // 2
        letra_igual = 0

        for i in range(meio):
            if dicio["pai"][i] == dicio["filho"][i]:
                letra_igual += 1
        
        res = (letra_igual / meio) * 100
        print(f"Compatibilidade: {res:.2f}%")
        
        if res >= 80:
            print("POTENCIAL PAI-FILHO")
            return True
        else:
            print("NÃO COMPATÍVEL")
            return False


def main():
    lista = [
        {"pai":"AACCTGGA", "filho": "AAGCTGGT"},
        {"pai":"ACGTACGT", "filho": "ACGAACGA"},
        {"pai":"AGCTA", "filho": "AGGTA"},
        {"pai":"ACGTACGTACGTACG", "filho": "ACGTATGTACGTACG"},
        {"pai":"ACGTACGTACGTACG", "filho": "ACGAATGTACGTACG"},
        {"pai":"AACCTGGA", "filho": "AAGCTG"}
    ]
    
    for dicio in lista:
        print(f"Possível Pai: {dicio['pai']}")
        print(f"Filho: {dicio['filho']}")
        verificar([dicio])
        print()


if __name__ == '__main__':
    main()

'''Uma cifra de César é uma forma fraca de criptografia que implica “rotacionar” cada letra por um número fixo de lugares. Rotacionar uma letra significa deslocá-la pelo alfabeto, voltando ao início se necessário, portanto ‘A’ rotacionado por 3 é ‘D’ e ‘Z’ rotacionado por 1 é ‘A’. Para rotacionar uma palavra, faça cada letra se mover pela mesma quantidade de posições. Por exemplo, “cheer” rotacionado por 7 é “jolly” e “melon” rotacionado por -10 é “cubed”. No filme 2001: Uma odisseia no espaço, o computador da nave chama-se HAL, que é IBM rotacionado por -1.
Escreva uma função chamada rotacionar() ->chamei de criptografar<- que receba uma string e um número inteiro como parâmetros, e retorne uma nova string que contém as letras da string original
rotacionadas pelo número dado.'''

#função criptografar/rotacionar
def criptografar(texto: str, deslocamento: str) -> str:
    aux = ""
    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra)
            aux += chr((((codigo - 97) + deslocamento) % 26) + 97)
# se a letra é z e o deslocamento 2, o código = 122, 122 = z da ASCII e 97 = a da ASCII (isso nos dá o número da letra dentro do alfabeto) + 2 (dá o intervalo dentro do alfabeto) + 97 (soma de volta aquilo que foi tirado no início) -> LEMBRA: números menores que 26 não dá p fazer "% 26" ent o resultado fica ele mesmo!
        else: aux += letra
    return aux

def descriptografar(texto_cripto: str, deslocamento: str) -> str:
    # retunr criprtografar (texto_cripto, - deslocamento)
    aux = ""
    for letra in texto_cripto:
        if letra.isalpha():
            codigo = ord(letra)
            aux += chr((((codigo - 97) - deslocamento) % 26) + 97)
        else: aux += letra
    return aux
# para descriptografar é só subtrair o deslocamento feito na cripto
    
#função principal     
def main(): 
    texto = input("Insira a frase: ").lower()
    deslocamento = int(input("Insira o nm de deslocamento: "))
    
    tt_cripto = criptografar(texto, deslocamento)
    print(f"Criptografada: {tt_cripto}")
    
    tt_descripto = descriptografar(tt_cripto, deslocamento)
    print(f"Descriptografada: {tt_descripto}")

#programa principal
if __name__ == '__main__':
    main()

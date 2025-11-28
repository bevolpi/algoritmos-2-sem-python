class Aluno:
    '''#variáveis de instância/atributos do objeto
    nome : str # *
    ra : int
    nota1 : float
    nota2 : float''' #nao precisa falar os atributos se já colocou os parametros la embaixo
    
    #construtor -> quando quero receber valores e a função no outro arquivo possa ter parâmetros!
    def __init__(self,  nome = '', ra = 0, nota1 = 0, nota2 = 0):
        self.nome = nome # quando coloca o "self." entende que ele ta pegando o ATRIBUTO do objeto (aquele lá de cima com um *)
            # o self.nome é o com *, e o = nome é o parâmetro passado
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        
    # método para calcular e retornar a média simples
    def calcular_media(self) -> float:
        return (self.nota1 + self.nota2) / 2
    
    #método para retornar a situação do aluno (aprovado ou reprovado)
    def situacao(self) -> str:
        media = self.calcular_media()
        if media >= 7.0:
            return 'APROVADO'
        return 'REPROVADO'
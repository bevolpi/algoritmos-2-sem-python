'''from aluno import Aluno

a = Aluno() #esse é um objeto com o endereço proprio
humberto = Aluno() #esse é outro

print(a)
# <aluno.Aluno object at 0x000001EE58D46A50>
# o print a -> variável a é um aluno, formato de objeto, em 0x (hexadecimal)
    #  hexadecimal = 16 -> 0-9...10 = A, 11 = B, 12 = C, 13 = D, 14 = E, 15 = F
        # a variavel a armazena o endereço do objeto!! (variável de referencia)
        
a.nome = 'selmini'
a.ra = 44
    #SÓ PRECISA DISSO SE NAO TEM O __init__ LÁ NO OUTRO ARQUIVO!
print(a.nome)'''

###################################

from aluno import Aluno
import aluno

a = Aluno('selmini', 44, 5, 10)
b = Aluno()

a_media = a.calcular_media()
a_status = a.situacao()

print(f"referência do objeto: {a}")
print(f"nome a: {a.nome}")
print(f"ra b: {b.ra}")
print(f"media a: {a_media}")
print(f"situação a: {a_status}")
import random

#sortear e mostrar o nome, 4 pessoas.

n1 = str(input('Qual o primeiro aluno:'))
n2 = str(input('Qual o segundo aluno:'))
n3 = str(input('Qual o terceiro aluno:'))
n4 = str(input('Qual o quarto aluno:'))
#para fazer a lista usa []
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}.'.format(escolhido))

'''dentro do random pode importar só o choice, ai ficaria from random import choice e embaixo tirar a referencia'''




import random
#seria correto usar só o from random import shuffle

#ler o nome dos alunos e a ordem sorteada

n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
#lista entre []
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)

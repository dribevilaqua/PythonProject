n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print('\nOs números digitados foram {}.'.format(n))
print('O valor 9 apareceu {} vezes.'.format(n.count(9)))
if 3 in n:
    print('O valor 3 apareceu na {}ª posição.'.format(n.index(3)+1))
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end=' ')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
print('\n')

'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

from random import randint
n = (randint(1,99),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os números são {}'.format(n))
ordem =  sorted(n)
print(ordem)
print("O maior é {} ".format(max(n)))
print("O menor é {} ".format(min(n)))


n = ((randint(1,99)),
(randint(1,99)),
(randint(1,99)),
(randint(1,99)),
(randint(1,99)))
print('Os números são {}'.format(n))
print('O maior valor gerado foi {}.'.format(max(n)))
print('O menor valor gerado foi {}.'.format(min(n)))
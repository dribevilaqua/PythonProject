from datetime import date
atual = date.today().year
nascimento = int(input('Qual ano do seu nascimento? '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade > 18 :
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
elif idade == 18 :
    print('Hora de se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, \nAinda falta {} para se alistar no serviço militar.'.format(saldo))


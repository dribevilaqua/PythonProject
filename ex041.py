from datetime import date
ano = int(input('Qual o ano do nascimento do atleta? '))
idade = date.today().year - ano
print('Sua idade é {} anos'.format(idade))
print('Segundo a Confederação Nacional de Natação, \nA sua categoria é:')
if idade <= 9 :
    print('MIRIM')
elif idade > 9 and idade <= 14 :
    print('INFANTIL')
elif idade > 14 and idade <= 19 :
    print('JUNIOR')
elif idade == 25 :
    print('SENIOR')
else :
    print('MASTER')
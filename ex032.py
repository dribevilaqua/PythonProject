from datetime import date
ano = int(input('Que ano você quer analisar? Para analisar o ano atual coloque 0: '))
#para verificar se o ano é bissexto, é so calcular se o ano é divisivil por 4 e os anos bissextos são aqueles múltiplos de 4, ou seja, a cada quatro anos temos um ano bissexto. Por outro lado, esses anos não são múltiplos de 100 (por exemplo,1800, 1900, 2100), exceto os múltiplos de 400 (por exemplo, 1600, 2000, 2400).
if ano == 0:
    ano = date.today().year
    ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
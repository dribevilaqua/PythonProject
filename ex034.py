salário = float(input('Qual o salário do funcionário? R$ '))
if salário <= 1250.00:
    aumento = salário * 1.15
else:
    aumento = salário * 1.10
print('Seu salário com o aumento será R$ {:.2f}'.format(aumento))

dias = float(input('Quantos dias o carro ficou alugado: '))
km = float(input('Quantos Km foram rodados: '))
valor = (dias*60.00)+(km*0.15)
print('O total a pagar é de R$ {:.2f}.'.format(valor))



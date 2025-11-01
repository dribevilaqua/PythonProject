print('Seja bem vindo cliente!')
casa = float(input('Qual valor da casa que você deseja financiar? R$ '))
salário = float(input('Qual sua renda mensa? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
parcela = casa / (anos * 12)
trinta = salário * 0.30
#Será aprovado o financiamento se o valor da parcela não exceder 30% do salário
print('Para pagar uma casa de R${:.2f} em {} anos, \na prestação será de {:.2f}'.format(casa, anos, parcela))
if parcela > trinta:
    print('No momento, não foi possível aprovar o financiamento.')
else :
    print('Seu financiamento foi aprovado.')


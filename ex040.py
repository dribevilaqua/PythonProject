nota1 = float(input('Qual a nota do primeiro semestre? '))
nota2 = float(input('Qual a nota do segundo semestre? '))
nota = (nota1 + nota2) / 2
print('Sua média foi {:.1f}'.format(nota))
print('Você está:')
if nota < 5 :
    print('REPROVADO')
elif nota >= 5.0 and nota < 7 :
    print('de RECUPERAÇÃO')
else :
    print('APROVADO')
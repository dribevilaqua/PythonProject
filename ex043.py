peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura**2)
print('Seu IMC é {:.2f}, '.format(imc), end='')
if imc < 18.5 :
    print('você está ABAIXO do peso.')
elif imc < 25 :
    print('você está no PESO IDEAL.')
elif imc < 30 :
    print('você está com SOBREPESO.')
elif imc <40 :
    print('você está com OBESIDADE.')
else :
    print('você está com OBESIDADE MORBIDA')
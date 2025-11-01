carro = float(input('Qual velocidade atual do seu carro?:'))
if carro <= 80:
    print('Você está dentro da velocidade permitida!')
else:
    print('Você ultrapassou a velocidade permitida de 80km/h!')
    print('Será multado em {:.2f} reais!'.format((carro-80)*7))
#pode usar também: multa = (carro-80) *7
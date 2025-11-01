num = int(input('Digite um número:'))
n = str(num)
print('Analisando o número {}:'.format(num))
print('Unidade:{}'.format(n[3]))
print('Centena: {}'.format(n[2]))
print('Dezena:{}'.format(n[1]))
print('Milhar:{}'.format(n[0]))

num = int(input('Informe um número:'))
u = num//1%10
c = num//10%10
d = num//100 % 10
m = num//1000 % 10
print('Analisando o número:{} \n Unidade é: {} \n Centena é: {} \n Dezena é {} \n Milhar é: {} '.format(num, u, c, d, m))
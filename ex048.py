soma = 0
#usando acumulador
cont = 0
#contador
for n in range (1, 501, 2):
    if n % 3 == 0:
        print(n, end=" ")
        soma = soma + n
        cont = cont + 1
print('\n A soma dos números de 1 até 500 que são impares é multiplos de três é: {}, foram {} números.'.format(soma, cont))


#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
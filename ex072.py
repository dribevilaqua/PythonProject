t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n = int(input("Digite um número (0 a 10): "))
    if 0 <= n <= 10:
        break
    print("Digite novamente")
print('Você digitou o número {}'.format(t[n]))




'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
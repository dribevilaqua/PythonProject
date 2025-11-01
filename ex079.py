numero = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado!')
    else:
        print("Valor duplicado, não será adicionado!")
    r = str(input("Quer continuar? [S/N] "))
    if r in 'Nn':
        break
print('-'*30)
numero.sort()
print(f'Você digitou os valores: {numero}')
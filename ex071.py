print('='*30)
print('{:^30}'.format('BANCO'))
print('='*30)
valor = int(input("Qual valor você quer sacar? R$ "))
total = valor
ced = 50
cont = 0
while True:
    if total >= ced:
        total = total - ced
        cont = cont + 1
    else:
        if cont > 0:
            print("Total de Celulas {} de R$ {}".format(cont, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            break




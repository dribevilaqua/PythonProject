total = 0
mil = 0
menor = cont = 0
barato = ' '
print("-"*20)
print('-'*6,'LOJÃO','-'*6)
print("-"*20)
while True:
    prod = str(input("Nome do produto: "))
    preco = float(input("Preço: R$ "))
    cont = cont + 1
    if cont == 1:
        menor = preco
        barato = prod
    else:
        if preco < menor:
            menor = preco
            barato = prod
    if preco > 1000:
        mil = 0 + 1
    total = total + preco
    sair = ' '
    while sair not in 'SN':
       sair = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if sair == 'N':
        break
print('----------------FIM--------------')
print("O total da compra foi {}.\nProdutos acima do valor de R$ 1000,00: {}\nO produto mais barato é: {}".format(total,mil, barato))




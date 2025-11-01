listagem = ('Lápis', 1.75,
            'Caderno', 15.90,
            'Borracha', 2,
            'Livro', 134.99,
            'Estojo', 25)
print('\n')
print('-'*40)
print(f'{'LISTAGEM DE PRODUTOS:':^40}' '\n')
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end=' ')
    else:
        print(f'R${listagem[item]:>7.2f}')
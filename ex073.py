times = ('Flamento', 'Palmeiras', 'Botafogo','Bahia', 'Atletico', 'São Paulo','Cruzeiro', "Fortaleza", 'Bragantino', "Internacional" )
print("Os cinco primeiros times são: ")
print('{}'.format(times[0:5]))
print('-'*30)
print('Os quatro ultimos são: ')
print('{}'.format(times[-4:]))
print('-'*30)
print('Os times em ordem alfabetica: \n{}'.format(sorted(times)))
print('-'*30)
print('A posição do São Paulo é {}º posição'.format(times.index('São Paulo')+1))
print('-'*30)
for t in times:
    print(t)



'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.'''
distância = float(input('Qual a distância da sua viagem? '))
#será cobrado valor diferente para viagens acima de 200 km
if distância <= 200:
    print('Sua viagem é de {} Km, \nSerá cobrado o valor de R$ 0.50 por Km \nSendo assim, será cobrado R$ {:.2f}'.format(distância, distância*0.50))
else:
    print('Sua viagem é de {} Km, \nSerá cobrado o valor de R$ 0.45 por Km \nSendo assim, será cobrado R$ {:.2f}'.format(distância, distância*0.45))
#pode usar com fórmula: preço = distância * 0.50
#outra opção: preço = distância * 0.50 if distância <= 200 else distância * 0.45
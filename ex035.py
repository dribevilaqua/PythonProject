#Para sabermos se tres medidas pode formar um triângulo, usamos a regra que cada segmento (medida) tem que ser menor que a soma dos outros segmentos (medidas).
print('-=='*20)
print('Analisador de triângulos')
print('-=='*20)
r1 = float(input('Primeiro segmento: '))
r2 =float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima NÃO podem formar triângulo!')
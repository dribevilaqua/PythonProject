import math

#Calcular seno, cosseno e tangente.

a = float(input('Digite um angulo:'))
#na formula abaixo o angulo precisa ser convertido para radiano para o calculo dar certo.
seno = math.sin(math.radians((a)))
print('O ângulo {} tem o seno de {:.2f}'.format(a, seno))
cosseno = math.cos(math.radians(a))
print('O ângulo {} tem o cosceno de {:.2f}'.format(a, cosseno))
tangente = math.tan(math.radians(a))
print('O ângulo {} tem o tangente de {:.2f}'.format(a, tangente))

#se não fosse usar a importação do math tudo e importar apenas o que vai usar:
#from math import radians, sin, cos, tan (nesse caso tira as referencias ao math
'''a = float(input('Digite um angulo:'))
#na formula abaixo o angulo precisa ser convertido para radiano para o calculo dar certo.
seno = sin(math.radians((a)))
print('O ângulo {} tem o seno de {:.2f}'.format(a, seno))
cosseno = cos(math.radians(a))
print('O ângulo {} tem o cosceno de {:.2f}'.format(a, cosseno))
tangente = tan(math.radians(a))
print('O ângulo {} tem o tangente de {:.2f}'.format(a, tangente))'''




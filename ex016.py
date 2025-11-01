import math

#ler número real e mostrar porção inteira, ex 7.97655 tem que aparecer 7

n = float(input("Digite um número decimal:"))
print('A porção inteira é:{}'.format(math.ceil(n)))

n1 = float(input("Digite um número decimal:"))
print('A porção inteira é:{}'.format(math.trunc(n1)))

'''Se fosse para importar apenas o trunc, em cima na importação seria:
from math import trunc
e na formula não usaria o math.
ficaria: 
n1 = float(input("Digite um número decimal:"))
print('A porção inteira é:{}'.format(math.trunc(n1)))'''

#ceil arrendonda, trunc corta o número no .
#outra forma de fazer sem importar math e usar trunc e usar int, que é outra opção de porção inteira.


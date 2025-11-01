n1=int(input('Digite um número:'))
n2=int(input('Digite outor número:'))
s=n1+n2
print('A soma dos números {}+{} é {}'.format(n1, n2, s))

algo = input('Digite algo:')
print('O que foi digitado é de qual tipo primitivo', type(algo))
print('O que foi digitado é apenas números?', algo.isnumeric())
print('O que foi digitado é apenas letras?', algo.isalpha())
print('O que foi digitado possui letras e números, ou seja é alfanúmerico?',algo.isalnum())
print('O que foi digitado possui letras apenas em minúsculo?', algo.islower())
print('Está apenas com letras maiusculas?', algo.isupper())
print("O que foi digitado possui números decimais?", algo.isdecimal())
print('O que foi digitado só tem espaços?', algo.isspace())
print('O que foi digitado está capitalizada, ou sejá não está apenas maiuscula nem apenas minuscula?', algo.istitle())


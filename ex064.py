n = int(input("Digite um número ou 999 para parar: "))
cont = 0
soma = 0

while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input("Digite um número ou 999 para parar: "))
print(cont, soma)

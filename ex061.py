print("Gerador de PA")
print("-="*10)
n = int(input("Escreva o primeiro número: "))
razao = int(input("Escreva a razão:"))
termo = n
cont = 1
while cont <= 10:
    print("{}".format(termo), end=' ')
    termo = termo + razao
    cont = cont+1
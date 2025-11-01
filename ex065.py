print("*"*10,"INICIO","*"*10,"\n")
soma = 0
contador = 0
r = "S"
maior = 0
menor = 0
while r != "N":
    n = int(input("Digite um número: "))
    soma = soma + n
    contador = contador + 1
    r = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if contador == 1:
         maior = n
         menor = n
    else:
        if (n > maior):
            maior = n
        if (n < menor):
            menor = n
print("\nA média dos número digitados foi: {} \nO maior número digitado foi {} \nO menor número digitado foi {}.".format(soma/contador, maior, menor))
print("\n","*"*10,"FIM","*"*10,"\n")






n = int(input("Qauntos termos você quer da fibonacci: "))
termo = 3
primeiro = 0
segundo = 1
soma = primeiro + segundo
print("-"*30)
print("Seguencia Fibonacci")
print("-"*30)
print("{} - {} - {}".format(primeiro, segundo, soma),end=' ')

while termo != n:
    primeiro = segundo
    segundo = soma
    soma = primeiro + segundo
    termo = termo +1
    print("- {}".format(soma), end=" ")
print('\nFIM')


n  = int(input('Digite um número: '))
print("____________________________")
print("A tabuada do numero {}:".format(n))
for c in range (0, 11):
    print('{} x {:2} = {}'.format(n, c, 1, n*c))

#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
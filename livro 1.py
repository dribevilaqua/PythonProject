lista = [1, 3, 5, 7, 9]
meio = 0
baixo = len(lista,0)
alto = len(lista)-1

item = int("Digite um número para busca:")

while baixo <= alto:
    meio = (baixo + alto)/2
    chute = lista[meio]
    if chute == item:
        return meio
    if chute > item:
        alto = meio
    else:
        baixo = meio +1
return None


print (len(lista, 3))
print (len(lista, -1))


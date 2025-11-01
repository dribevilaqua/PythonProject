from random import randint
print("Vamos jogar par ou ímpar: ")
v = 0
while True:
    c = randint(0,11)
    j = int(input("Digite um número: "))
    e = ' '
    r = c + j
    while e not in 'PI':
        e = str(input("Par ou Impar [P/I]: ")).upper().strip()[0]
        print("Você jogou {} e o computador {}, total {}.".format(j, c, r))
    if e == 'P':
        if r %2 == 0:
             print("Você venceu!")
             v = v +1
        else:
            print("Você perdeu!")
            break
    elif e == 'I':
        if r % 2 == 1:
            print("Você venceu!")
            v = v + 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente!")
print("GAMER OVER, você venceu {} vezes.".format(v))


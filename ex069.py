maior = 0
h = 0
m = 0
while True:
    print("-"*20)
    print("CADASTRE UMA PESSOA")
    print("-"*20)
    i = int(input("Idade: "))
    if i > 18:
        maior = maior + 1
    s = ' '
    while s not in 'MF':
        s = str(input("Sexo [M/F]: ")).upper().strip()[0]
    if s == 'M':
        h = h + 1
    if s == 'F' and i < 20:
        m = m + 1
    print("-" * 20)
    c = ' '
    while c not in 'SN':
        c = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    if c == 'N':
        break
print("{} pessoas tem mais de 18 anos.\n{} são homens.\n{} são mulheres com menos de 20 anos\n".format(maior, h, m))

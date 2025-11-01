while True:
    n = int(input("Digite um número para a tabuada: "))
    if n < 0:
        break
    print("-" * 30)
    for c in range (1 , 11):
        print("{} x {} = {}".format(n,c , n*c))
    print("-" * 30)
print("\nPrograma encerrado, volte sempre!")


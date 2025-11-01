print("CALCULADORA")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = int(input("Qual operação deseja realizar? \n1-Adição \n2-Subtração \n3-Divisão \n4-Multiplicação\n"))
if op == 1:
    print(n1 + n2)
elif op == 2:
    print(n1 - n2)
elif op == 3:
    if n2 != 0:
        print(n1 / n2)
    else:
        print("Não é possivel divisão por zero!")
elif op == 4:
    print(n1 * n2)
else:
    print("Opção inválida!")

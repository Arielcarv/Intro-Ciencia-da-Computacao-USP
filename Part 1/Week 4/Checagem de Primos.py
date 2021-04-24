inteiro = int(input("Digite um número inteiro: "))

i = 1


if inteiro > 1:
    for i in range(2, inteiro):
        if (inteiro % i) == 0:
            print("não primo")
            break
    else:
        print("primo")
else:
    print("não primo")

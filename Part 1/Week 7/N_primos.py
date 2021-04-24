def isPrime(inteiro):
    check = False
    if inteiro > 1:
        for i in range(2, inteiro):
            if (inteiro % i) == 0:
                # print("não primo")
                return check
        else:
            check = True
            # print("primo")
            return check
    else:
        # print("não primo")
        return check


def n_primos(integer):
    var1 = 2
    soma = 0
    while var1 <= integer:
        if isPrime(var1):
            soma += 1
        var1 += 1
    return soma


integer = 0
while integer < 2:
    try:
        integer = int(input("Inteiro: "))
    except ValueError:
        print('Valor inválido')


print(n_primos(integer))

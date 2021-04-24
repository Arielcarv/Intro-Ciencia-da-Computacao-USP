def isPrime(inteiro):
    check = False
    if inteiro > 1:
        for i in range(2, inteiro):
            if (inteiro % i) == 0:
                #print("não primo")
                return check
        else:
            check = True
            #print("primo")
            return check
    else:
        #print("não primo")
        return check


def decompose_primes(n):
    factor = 2
    multiplicidade = 0
    while n > 1:
        while n % factor == 0:
            multiplicidade += 1
            n = n / factor

        if isPrime(factor):
            primo = "é primo"
        else:
            primo = "não é primo"

        if multiplicidade > 0:
            print(f"Fator: {factor} {primo}, multiplicidade = {multiplicidade}")

        factor += 1
        multiplicidade = 0


while True:
    try:
        number = int(input('Digite um numero inteiro > 1: '))
        decompose_primes(number)
    except ValueError:
        print('Ooops! Caracter inválido! Tente novamente')
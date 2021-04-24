def fatorial(num):
    result_fatorial = 1
    for i in range(1, num + 1):
        result_fatorial = result_fatorial * (num)
        num -= 1
    return result_fatorial

#print(fatorial(5))

def testa_fatorial():

    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")

testa_fatorial()

def numero_binomial (n, k):
    return fatorial(n) // (fatorial(k)*(fatorial(n-k)))

print(numero_binomial(20,10))


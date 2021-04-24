import math


def e_hipotenusa(n):
    i = 1
    while i < n:
        j = 1
        while j < n:
            if n == math.sqrt(i ** 2 + j ** 2):
                return True
            j = j + 1
        i = i + 1
    return False


def soma_hipotenusas(n):
    count = 1
    soma = 0
    while count <= n:
        if e_hipotenusa(count):
            soma = soma + count
        count += 1
    return soma


number = int(input('Numero: '))

print(soma_hipotenusas(number))

def fatorial(number):
    fatorial = 1
    while number > 1:
        fatorial = fatorial * number
        number -= 1
    return fatorial


while True:
    try:
        number = int(input("Digite um numero inteiro positivo: "))
        print(fatorial(number))
        if number < 0:
            break
    except ValueError:
        print("Ooops. Numero não válido! Tente novamente")


'''number = int(input("Type a number: "))

while number > 0:
    print(number % 10)
    #print(number_1)
    number = (number // 10)


decrescente = True
valor = 1
anterior = int(input("Type the first number of the sequence: "))

while valor != 0 and decrescente:
    valor = int(input("Type the next sequence number: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente == True:
    print("The sequence is in decrescent order.")
else:
    print("The sequence is in crescent order.")


meuCartão = int(input("Credit Card Number: "))

cartaoLido = 1
encontreiMeuCartãoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartãoNaLista:
    cartaoLido = int(input("Type the next Credit Card number: "))
    if cartaoLido == meuCartão:
        encontreiMeuCartãoNaLista = True

if encontreiMeuCartãoNaLista:
    print("Yeah!")
else:
    print("Not Found/Lost")'''


# Dígitos adjacentes iguais

number = int(input("Type a number: "))
number_1 = 0

while number > 0:
    if number_1 == (number % 10):
        print(f"Há numeros adjacentes iguais: {number_1}")
    number_1 = number % 10
    print(number_1)
    #print(number_1)
    number = (number // 10)


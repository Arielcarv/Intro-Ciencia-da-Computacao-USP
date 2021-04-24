lista = []
num = 1

while num != 0:
    try:
        num = int(input("Digite um número:"))
        lista.append(num)
    except ValueError:
        print("Valor inválido!")

# print(lista)

for i in range(len(lista)):
    # print(i)
    if lista[-1-i] != 0:
        print(lista[-1-i])

    i -= 1

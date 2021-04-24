def input_natural():
    num = int(input("Digite o valor de n: "))
    return num


num = input_natural()

fatorial = 1

if num < 0:
    input_natural()
else:
    for i in range(1, num+1):
        fatorial += fatorial * (num - i)


print(fatorial)

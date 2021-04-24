inteiro = int(input("Digite um número inteiro: "))

adj = 0
char = 0

adjacente = False

while inteiro > 0:
    char = inteiro % 10
    resto = inteiro // 10
    adj = resto % 10
    if char == adj:
        adjacente = True
        break
    inteiro = resto

if adjacente:
    print("sim")
else:
    print("não")




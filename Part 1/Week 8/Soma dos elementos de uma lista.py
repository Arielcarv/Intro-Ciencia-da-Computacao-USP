lista = [2, 4, 2, 2, 3, 3, 1]

def soma_elementos(lista):
    soma = 0
    for element in lista:
        soma += element
    return soma

print(soma_elementos(lista))
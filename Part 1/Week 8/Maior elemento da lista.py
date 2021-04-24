def maior_elemento(lista):
    maior = -999
    for item in lista:
        if item > maior:
            maior = item

    return maior
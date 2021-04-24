def ordenada(lista):
    ordem = True
    for index in range(len(lista)-1):
        if lista[index] > lista[index + 1]:
            ordem = False
    return ordem


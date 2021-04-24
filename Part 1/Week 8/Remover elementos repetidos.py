# lista = [2, 4, 2, 2, 3, 3, 1]

def remove_repetidos(lista):
    lista_aux = []
    for element in lista:
        if element not in lista_aux:
            lista_aux.append(element)

    return sorted(lista_aux)

# print(remove_repetidos(lista))


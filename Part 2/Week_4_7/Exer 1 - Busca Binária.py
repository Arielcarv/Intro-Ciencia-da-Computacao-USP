# lista1 = ['a','e','i']
# lista2 = [1, 2, 3, 4, 5]
# lista3 = [1, 2, 3, 4, 5, 6]


def busca (lista, elemento):
    primeiro = 0
    ultimo = len(lista)-1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == elemento:
            print(meio)
            return meio
        else:
            if elemento < lista[meio]:
                print(meio)
                ultimo = meio - 1
            else:
                print(meio)
                primeiro = meio + 1
    return False


# busca(lista1, 'e')
# busca(lista2, 6)
# busca(lista3, 4)
# a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]


def encontra_impares(lista):
    if not lista:
        return[]
    if lista[0] % 2 == 1:
        return[lista[0]] + encontra_impares(lista[1:])
    return encontra_impares(lista[1:])

# print(encontra_impares(a))
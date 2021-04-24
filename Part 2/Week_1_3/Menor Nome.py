
def menor_nome (lista):
    indice = 0
    total = len(lista)
    menor = lista[0]

    while indice < total:
        if len(menor) > len(lista[indice].strip()):
            menor = lista[indice].strip()
            indice += 1
        else:
            indice += 1

    return menor.capitalize()

lista1 = (['maria', 'josé', 'PAULO', 'Catarina'])
# # deve devolver 'José'

lista2 = (['maria', ' josé  ', '  PAULO', 'Catarina  '])
# # deve devolver 'José'

lista3 = (['Bárbara', 'JOSÉ  ', 'Bill'])
# # deve devolver José

print(menor_nome(lista1))
print(menor_nome(lista2))
print(menor_nome(lista3))
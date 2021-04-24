#  Clone lists

def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone

lista1 = ["vermelho", "verde", "azul"]

lista2 = clone(lista1)

print(lista1)
lista2[0] = "rosa"
print(lista2)

# Fatiamento
# lista[ini:fim]
# lista[ini:]
# lista[:fim]

# Clone List
# lista[:]

del lista2[1]
lista2[0] = "rosa"
print(lista2)

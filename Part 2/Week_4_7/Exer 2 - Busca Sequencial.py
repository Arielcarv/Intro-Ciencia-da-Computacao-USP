def busca(lista, elemento):
    for index in range(len(lista)):
        if lista[index] == elemento: 
            return index
    return False

print(busca(['a', 'e', 'i'], 'e'))
# deve devolver => 1

print(busca([12, 13, 14], 15))
# deve devolver => False
import random

def lista_grande(n):
    lista = [random.randrange(10000) for x in range(n)] # inteiros entre 0 e 999
    return lista

# print(lista_grande(10))
def fatorial(n):
    if n < 1:                   # base da recursão
        return 1
    else:
        return n * fatorial(n-1) # chamada recursiva

def fibonacci(n):
    if n < 2: 
        return n # base
    else:
        return fibonacci(n-1) + fibonacci(n-2) # chamada recursiva


def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1
    if max < min:
        return False
    else:
        meio = min + (max-min) // 2
    
    if lista[meio] > elemento:
        print('a')
        return busca_binaria(lista, elemento, min, meio-1)   
    elif lista[meio] < elemento:
        print('a')
        return busca_binaria(lista, elemento, meio+1, max)
    else:
        return meio

def merge_sort(lista):
    if len(lista) <= 1:     # base da recursão
        return lista

    meio = len(lista) // 2
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito
    
    if not lado_direito:
        return lado_esquerdo
    
    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge_sort(lado_esquerdo[1:], lado_direito)
    
    return[lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])


import pytest

@pytest.mark.parametrize("entrada1, saida1", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
    ])

def test_fatorial(entrada1, saida1):
    assert fatorial(entrada1) == saida1

@pytest.mark.parametrize("entrada2, saida2", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
    ])

def test_fibonacci(entrada2, saida2):
    assert fibonacci(entrada2) == saida2

a = [10, 20, 30, 40, 50, 60]
@pytest.mark.parametrize("entrada3, valor, saida3", [
    (a, 10, 0),
    (a, 20, 1),
    (a, 30, 2),
    (a, 40, 3),
    (a, 50, 4),
    (a, 60, 5),
    (a, 70, False),
    (a, 15, False),
    (a, -10, False),
])

def test_busca_binaria(entrada3, valor, saida3):
    assert busca_binaria(entrada3, valor) == saida3

busca_binaria([-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934], 99)
import dimensoes

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]


def soma_matrizes(m1, m2):
    if dimensoes.dimensoes(m1) == dimensoes.dimensoes(m2):
        for linha in range(len(m1)):
            for cell in range(len(m1[linha])):
                novo_valor = m1[linha][cell] + m2[linha][cell]
            
                m1[linha][cell] = novo_valor
    else:
        return False
    
    return m1

print(soma_matrizes(m1, m2))

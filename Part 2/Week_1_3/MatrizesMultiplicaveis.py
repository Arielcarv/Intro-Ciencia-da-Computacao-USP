m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
m3 = [[1], [2], [3]]
m4 = [[1, 2, 3]]
m5 = [[1]]
m6 = [[1, 2, 3]]
m7 = [[1], [2], [3]]
m8 = [[1, 2, 3], [4, 5, 6]]


def sao_multiplicaveis(m1, m2):
    print(len(m1[0]))
    print(len(m2))
    if len(m1[0]) == len(m2):
        return True
    else:
        return False

# print(sao_multiplicaveis(m1, m2))
# print(sao_multiplicaveis(m3, m4))
# print(sao_multiplicaveis(m5, m6))
print(sao_multiplicaveis(m7, m8))
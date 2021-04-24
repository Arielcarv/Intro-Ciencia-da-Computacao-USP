minha_matriz1 = [[1], [2], [3]]
minha_matriz2 = [[1, 2, 3], [4, 5, 6]]

def imprime_matriz(matriz):
    for i in matriz:
        linha = ''
        for j in i:
            linha += str(j)
        print(" ".join(linha), end="")  
        print()
    

# imprime_matriz(minha_matriz1)
# imprime_matriz(minha_matriz2)

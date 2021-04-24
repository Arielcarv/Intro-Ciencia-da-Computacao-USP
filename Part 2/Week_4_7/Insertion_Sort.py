def insertion_sort(lista): 
    for indice in range(1, len(lista)): 
  
        valor = lista[indice] 
        j = indice - 1
        while j >= 0 and valor < lista[j]:            
                lista[j + 1] = lista[j] 
                j -= 1
        lista[j+1] = valor 
    return lista

# arr = [12, 11, 13, 5, 6] 

# print(insertion_sort(arr))

def incomodam(n):
    if n <= 0:
        return ""           #Base 
    return "incomodam " + incomodam(n-1) #Recursividade


def elefantes(n, contador=0):
    contador += 1
    if n <= 0 or contador > n:
        return ""
    else:
        if contador == 1:
            return "Um elefante incomoda muita gente\n" + elefantes(n, contador)
        else:
            frase1 = str(contador) + " elefantes " + incomodam(contador) + "muito mais"
            if (n - contador == 0):
                return(frase1 + elefantes(n, contador))
            else:
                frase2 = "\n" + str(contador) + " elefantes incomodam muita gente\n"
                return (frase1 + frase2 + elefantes(n, contador))



# print(elefantes(4))

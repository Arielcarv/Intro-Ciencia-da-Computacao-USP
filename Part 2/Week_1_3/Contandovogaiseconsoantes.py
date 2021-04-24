
def conta_letras(frase, contar="vogais"):
    contagem = 0
    vogais = "aeiou"
    if contar == "vogais":
        for letra in frase.lower():
            if letra in vogais:
                contagem += 1
    elif contar == "consoantes":
        for letra in frase.lower():
            if (letra not in vogais) and (letra not in " "):
                contagem += 1
    return contagem

# print(conta_letras('programamos em python'))
# # deve devolver 6

# print(conta_letras('programamos em python', 'vogais'))
# # deve devolver 6

# print(conta_letras('programamos em python', 'consoantes'))
# # deve devolver 13

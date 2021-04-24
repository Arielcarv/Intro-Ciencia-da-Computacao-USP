

def primeiro_lex(lista):
    menor = min(lista)
    return menor



print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
# deve devolver 'A'

print(primeiro_lex(['AAAAAA', 'b']))
# deve devolver 'AAAAAA'
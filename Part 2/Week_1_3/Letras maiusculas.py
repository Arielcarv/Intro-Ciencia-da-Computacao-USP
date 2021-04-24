def maiusculas(string):
    uppercase_string = ''
    for letra in string:
        if letra.isupper():
            uppercase_string += letra
    return uppercase_string


maiusculas1 = ('Programamos em python 2?')
# deve devolver 'P'

maiusculas2 = ('Programamos em Python 3.')
# deve devolver 'PP'

maiusculas3 = ('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'

print(maiusculas(maiusculas1))
print(maiusculas(maiusculas2))
print(maiusculas(maiusculas3))
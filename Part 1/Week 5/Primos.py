def éPrimo(inteiro):
    check = False
    if inteiro > 1:
        for i in range(2, inteiro):
            if (inteiro % i) == 0:
                #print("não primo")
                return check
        else:
            check = True
            #print("primo")
            return check
    else:
        #print("não primo")
        return check


def maior_primo(a):
    primo = 0
    if a >= 2:
        for i in range(2, a+1):
            if éPrimo(i):
                primo = i
    return primo

def test_primo1():
    assert maior_primo(100) == 97

def test_primo2():
    assert maior_primo(7) == 7


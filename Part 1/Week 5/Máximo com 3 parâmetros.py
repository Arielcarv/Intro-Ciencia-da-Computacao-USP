def maximo(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def test_maximo1():
    assert maximo(30, 14, 10) == 30

def test_maximo2():
    assert maximo(0, -1, 1) == 1



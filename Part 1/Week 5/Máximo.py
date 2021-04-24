def maximo(a, b):
    if a > b:
        return a
    else:
        return b

def test_maximo1():
    assert maximo(3, 4) == 4

def test_maximo2():
    assert maximo(0, -1) == 0



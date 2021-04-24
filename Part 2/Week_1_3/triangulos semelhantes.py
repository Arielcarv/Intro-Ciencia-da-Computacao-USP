

class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def semelhantes(self, triangulo):

        a, b, c = triangulo.a, triangulo.b, triangulo.c
        
        if ((a % self.a) == 0 ) and ((b % self.b) == 0) and ((c % self.c) == 0):
            return True
        elif ((a // self.a) == 0 ) and ((b // self.b) == 0) and ((c // self.c) == 0):
            return True
        return False


# t1 = Triangulo(2, 2, 2)
# t2 = Triangulo(4, 4, 4)
# print(t1.semelhantes(t2))

# t3 = Triangulo(3, 4, 5)
# t4 = Triangulo(3, 4, 5)
# print(t3.semelhantes(t4))

# t5 = Triangulo(6, 8, 10)
# t6 = Triangulo(3, 4, 5)
# print(t5.semelhantes(t6))
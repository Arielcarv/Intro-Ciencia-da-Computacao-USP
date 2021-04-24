import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        if math.sqrt(self.a**2 + self.b**2) == self.c:
            return True
        return False
    
# t = Triangulo(1, 3, 5)
# print(t.retangulo())
# # deve devolver False

# u = Triangulo(3, 4, 5)
# print(u.retangulo())
# # deve devolver True
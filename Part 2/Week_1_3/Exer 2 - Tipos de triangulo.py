class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return ("equilátero")
        elif (self.a != self.b) and (self.a != self.c):
            return ("escaleno")
        else:
            return ("isósceles")



# t = Triangulo(4, 4, 4)
# print(t.tipo_lado())
# # deve devolver 'equilátero'

# u = Triangulo(3, 4, 5)
# print(u.tipo_lado())
# # deve devolver 'escaleno'
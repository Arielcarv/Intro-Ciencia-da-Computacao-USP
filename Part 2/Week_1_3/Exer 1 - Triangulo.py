class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro

# t = Triangulo(1, 1, 1)

# print(t.a)
# # deve devolver o valor do lado a do triângulo
# print(t.b)
# # deve devolver o valor do lado b do triângulo
# print(t.c)
# # deve devolver o valor do lado c do triângulo

# print(t.perimetro())
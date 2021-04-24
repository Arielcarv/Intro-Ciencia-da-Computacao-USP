import math

class Bhaskara:
    ## Functions
    def delta(self, a, b, c):
        return int((b ** 2 - 4 * a * c))

    # Inputs
    def main(self):
        a = float(input('Digite "a":'))
        b = float(input('Digite "b":'))
        c = float(input('Digite "c":'))
        print(self.calcula_raizes(a, b, c))


    # Print Roots
    def calcula_raizes(self, a, b, c):
        delt = self.delta(a, b, c)
        if delt == 0:
            raiz = (-b + math.sqrt(delt)) / (2 * a)
            return 1, raiz
        else:
            if delt < 0:
                return 0
            else:
                raiz1 = (-b + math.sqrt(delt)) / (2 * a)
                raiz2 = (-b - math.sqrt(delt)) / (2 * a)
                return 2, raiz1, raiz2


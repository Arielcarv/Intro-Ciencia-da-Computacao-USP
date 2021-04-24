import math

a = float(input('Digite "a":'))
b = float(input('Digite "b":'))
c = float(input('Digite "c":'))

delta = b**2 - 4*a*c

def raiz1(a,b,delta):
    raiz = (-b + math.sqrt(delta)) / (2 * a)
    return raiz
def raiz2(a,b,delta):
    raiz = (-b - math.sqrt(delta)) / (2 * a)
    return raiz

if delta == 0:
    print(f"a raiz desta equação é {raiz1(a,b,delta)}")
elif delta < 0 :
    print(f"esta equação não possui raízes reais")
else:
    if raiz1(a,b,delta) < raiz2(a,b,delta):
        print(f"as raízes desta equação são {raiz1(a,b,delta)} e {raiz2(a,b,delta)}")
    else:
        print(f"as raízes desta equação são {raiz2(a, b, delta)} e {raiz1(a, b, delta)}")


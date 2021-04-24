import math

x1 = int(input("1ª Coordenada x: "))
y1 = int(input("1ª Coordenada y: "))
x2 = int(input("2ª Coordenada x: "))
y2 = int(input("2ª Coordenada y: "))


def distancia(x1,y1, x2, y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist


if distancia(x1,y1,x2,y2) >= 10:
    print("longe")
else:
    print("perto")

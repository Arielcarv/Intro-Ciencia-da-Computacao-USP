largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

alt = altura
while alt > 0:
    lar = largura
    while lar > 0:
        if (lar != largura and lar != 1) and (alt != altura and alt != 1):
            print(' ', end='')
        else:
            print('#', end='')
        lar -= 1
    print()
    alt -= 1

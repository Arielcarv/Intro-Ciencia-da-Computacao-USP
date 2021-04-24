largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

while altura > 0:
    l = largura
    while l > 0:
        print('#', end='')
        l -= 1
    print()
    altura -= 1


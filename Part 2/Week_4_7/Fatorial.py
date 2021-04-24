def fatorial(x):
    if x < 1:                   # base da recursão
        return 1
    else:
        return x * fatorial(x-1) # chamada recursiva

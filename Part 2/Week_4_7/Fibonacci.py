
def fibonacci(n):
    if n < 2: 
        return n # base
    else:
        return fibonacci(n-2) + fibonacci(n-1) # chamada recursiva

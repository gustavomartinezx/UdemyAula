def soma(*args):
    print(*args)

soma(4, 5, 6)

def somar(*args):
    total = 0
    for x in args:
        total += x
    return total

resultado = somar(3, 2)
print(resultado)
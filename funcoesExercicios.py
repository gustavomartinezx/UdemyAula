def multiplique(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

print(multiplique(3, 4, 5))

def imparOuPar(x):
    if x % 2 == 0:
        return print("Par")
    else:
        return print("Impar")

imparOuPar(5)
def executa(funcao, *args):
    def interno(*args):
        return funcao(*args)
    return interno

def some(x, y):
    return x+y

soma_de_10 = executa(some, 10, 5)
print(soma_de_10)
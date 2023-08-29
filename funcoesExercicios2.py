def criar_multiplicador(multiplicador):
    def multiplicando(numero):
        return numero * multiplicador
    return multiplicando

duplica = criar_multiplicador(2)
print(duplica(3))
def unir_listas(l1, l2):
    intervalo_maximo = min(len(l1), len(l2))
    return [
            (l1[i], l2[i]) for i in range(intervalo_maximo)
    ]

l1 =['BA', 'SP', 'MG', 'RJ']
l2 = ['Salvador', 'Ubatuba', 'Belo Horizonte']

print((list(zip(l1,l2))))
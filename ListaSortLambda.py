lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

l1 = sorted(lista, key=lambda item: item['nome'])
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = lista.sort(key=lambda item: item['sobrenome'])



def exibir(lista):
    for elemento in lista:
        print(elemento)
    print()

exibir(l1)
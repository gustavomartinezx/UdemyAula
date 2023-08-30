import pprint
def print_lindo(v):
    pprint.pprint(v, sort_dicts=False, width=40)
lista = [
    {"carne": "vaca", "preco": "10,5"},
    {"carne": "galinha", "preco": "12,5"},
    {"carne": "boi", "preco": "15,5"}
]

# n antes do for vai ser a variavel chamada dentro da lista,
# após isso é o parametro para adição
# e depois do for é o filtro
lista_nova = [
    {**produto, 'carne': 'morcego'}
    if produto['carne'] == 'boi' else {**produto}
    for produto in lista
]
print_lindo(lista_nova)

l2 = [n for n in range(10) if n<5]
# 
# print(l2)
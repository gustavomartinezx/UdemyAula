pessoa = {
    "Nome": "Mirella",
    "Sobrenome": "Fonseca"
}

informacoes = {
    "Altura": "1.68",
    "Idade": "16",
}

informacoes_completas = {**pessoa, **informacoes}

print(informacoes_completas)
# a, b = pessoa.items()
# print(a, b)


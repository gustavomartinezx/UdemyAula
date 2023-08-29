contador = 1

perguntas = [
    {
        'pergunta': 'Quanto é 3x2',
        'opções': ['4', '5', '6', '7'],
        'resposta': '6',

    },
    {
        'pergunta': 'Quanto é 2x2',
        'opções': ['4', '10', '12', '16'],
        'resposta': '4',
    }
]

for pergunta in perguntas:
    contador = 1
    print(pergunta['pergunta'])
    print()

    for x in pergunta['opções']:
        print(str(contador) + ")" + str(x))
        contador += 1
    print()
    
    resposta = input("Coloque sua resposta: ")

    if resposta != pergunta['resposta']:
        print("Resposta errada ❌")
    else:
        print("Resposta correta ✔️")
    print()
lista = []

while True:
    indice = None
    menu = input("""
    Selecione uma opção
    [a]pagar [i]nserir [l]istar
    """).lower()

    if menu != "a" and menu != "i" and menu != "l":
        continue
    
    ### sistema de apagar
    if menu == "a":
        for indiceDaLista, itemDaLista in enumerate(lista): 
            print(indiceDaLista, itemDaLista)
            
        indice = int(input("Insira o indice que queira apagar!"))

        if  indice >= len(lista):
            print("Indice errado")
        else:
            lista.pop(indice)

    ### sistema de inserir
    if menu == "i":
        itemAppendDaLista = input("Insira o item a ser adicionado da lista: ")
        lista.append(itemAppendDaLista)

    ### sistema de listagem
    if menu == "l":
        for indiceDaLista, itemDaLista in enumerate(lista): 
            print(indiceDaLista, itemDaLista)
"""

numeroEscolhido = input("Insira um número: ")
verificaSeEPar = None

try:
    numeroEscolhidoTransformadoEmFloat = float(numeroEscolhido)
    verificaSeEPar = numeroEscolhidoTransformadoEmFloat % 2
    if verificaSeEPar == 0:
        print("Par")
    else:
        print("Impar")
except:
    print("Não é um número!")
"""

hora = int(input("Insira o seu horário: "))

bomDia = hora >= 0 and hora <= 11
boaTarde = hora >= 12 and hora <= 17
boaNoite = hora >= 18 and hora <= 23

if bomDia:
    print("Bom Dia")
elif boaTarde:
    print("Boa Tarde")
else:
    print("Boa Noite")
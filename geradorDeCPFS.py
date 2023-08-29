cpf = input("Insira os digitos do CPF: ")
ponto = "."
cpfSemPontos = ""
somaDosNovesPrimeirosDigitos = 0
cpfConCatenado = None
doisNumerosFinais = None
cpfNumeros = []
cpfNumerosINT = []
multiplicando = 10
resultadoDaSomaMultiplicadaPorDez = 0
restoDaDivisao = 0
resultadoPrimeiroNumero = 0
stringConversaoPrimeiroNumero = None

###segundo digito
multiplicandoSegundoDigito = 11
resultadoSegundoDigito = 0
somaDosDezPrimeirosDigitos = 0
resultadoDoSegundoNumero = 0
stringConversaoSegundoNumero = None

### REMOÇÃO DE PONTOS
for numerosNoCPF in cpf:
    if ponto == numerosNoCPF:
        continue
    else: 
        cpfSemPontos += numerosNoCPF

### colocando em lista
for itens in cpfSemPontos:
    cpfNumeros += itens

### transformando a lista em int
for itensDaLista in cpfNumeros:
    intItensDaLista = int(itensDaLista)
    cpfNumerosINT.append(intItensDaLista)

print(type(cpfNumerosINT[0]))
print(cpfNumerosINT)

### multiplicacao

for numerosDaLista in cpfNumerosINT:
    resultado = numerosDaLista * multiplicando
    somaDosNovesPrimeirosDigitos += resultado
    multiplicando = multiplicando - 1
    resultado = 0 

print(somaDosNovesPrimeirosDigitos)

resultadoDaSomaMultiplicadaPorDez = somaDosNovesPrimeirosDigitos * 10
restoDaDivisao = resultadoDaSomaMultiplicadaPorDez % 11

if restoDaDivisao > 9:
    resultadoPrimeiroNumero = 0
else:
    resultadoPrimeiroNumero = restoDaDivisao

print(resultadoPrimeiroNumero)

cpfNumerosINT.insert(0, resultadoPrimeiroNumero)
for numerosDaLista in cpfNumerosINT:
    resultadoSegundoDigito = numerosDaLista * multiplicandoSegundoDigito
    somaDosDezPrimeirosDigitos += resultado
    multiplicandoSegundoDigito = multiplicandoSegundoDigito - 1
    resultado = 0 

resultadoDaSomaMultiplicadaPorDezDoisDigitos = somaDosDezPrimeirosDigitos * 10
restoDaDivisaoSegundoDigito = resultadoDaSomaMultiplicadaPorDezDoisDigitos %11

if restoDaDivisaoSegundoDigito > 9:
    resultadoDoSegundoNumero = 0
else:
    resultadoDoSegundoNumero = restoDaDivisao
stringConversaoPrimeiroNumero = str(resultadoPrimeiroNumero)
stringConversaoSegundoNumero = str(resultadoSegundoNumero)

doisNumerosFinais = [resultadoPrimeiroNumero, resultadoDoSegundoNumero]
cpfSemPontos.join(doisNumerosFinais)
print(cpfSemPontos)
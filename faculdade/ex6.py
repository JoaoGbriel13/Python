tamanho = int(input('Digite o tamanho da lista: '))
count = 0
listaPadrao = []
listaRepetidos = []
while count < tamanho :
    numero = int(input('Digite o numero que deseja colocar na lista: ')) 
    if numero not in listaPadrao :
        listaPadrao.append(numero)
    elif numero in listaPadrao :
        listaRepetidos.append(numero)
    count = count + 1



print(listaPadrao)
print(listaRepetidos)

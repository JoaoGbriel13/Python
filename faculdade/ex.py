


nA = int(input('Digite o tamanho da primeira lista: '))

i = 0
i2 = 0
lista1 = []
lista2 = []


while i < nA : 
    nlista = int(input('Digite o numero que deseja adicionar : '))
    if nlista not in lista1 :
        lista1.append(nlista)
    else:
        print("Você precisa digitar um numero que ainda não colocou!")
        continue
    i = i + 1


nB = int(input('Digite o tamanho da segunda lista: '))

while i2 < nB : 
    nlista = int(input('Digite o numero que deseja adicionar : '))
    if nlista not in lista2 :
        lista2.append(nlista)
    else:
        print("Você precisa digitar um numero que ainda não colocou!")
        continue
    i2 = i2 + 1

listaFinal = lista1 + lista2

def criarListaFinal(lista) :
    lF = []
    for i in lista :
        if i not in lF:
            lF.append(i)
    print(lF)

criarListaFinal(listaFinal)



    







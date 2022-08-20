#Criando lista e separando através de numeros positivos e negativos
i = 0 
listaCompleta = []

tamanho = int(input('Escreva o tamanho da sua lista: '))

while i < tamanho :
    N = int(input("Digite os numeros que deseja introduzir a lista: "))
    if N <50 :
        listaCompleta.append(N)
        i = i + 1
    else:
        print('Você precisa digitar um numero entre 0 e 50')
        continue

print(listaCompleta)

listaPositiva = []
listaNegativa = []
for n in listaCompleta :
    if n > 0:
        listaPositiva.append(n)
    else:
        listaNegativa.append(n)

print(listaPositiva)
print(listaNegativa)
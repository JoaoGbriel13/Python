import random


tamanho = int(input("Insira o tamanho da lista: "))
i = 0
listaAleatorios = []
while i < tamanho :
    listaAleatorios.append(random.randint(1,50))
    i = i + 1

print(listaAleatorios)

checagem = int(input('Escreva o numero que deseja encontrar : '))

while checagem > 0 :
    if checagem in listaAleatorios :
        listaAleatorios.remove(checagem)
        print('Numero removido com sucesso!')
        checagem = 0


print(listaAleatorios)




    


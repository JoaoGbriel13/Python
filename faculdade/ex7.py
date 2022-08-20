import enum
from operator import index, indexOf
import random

tamanho = int(input('Digite o tamanho da lista: '))
listaNumeros = []
count = 0

if tamanho < 5000 :
    print('Você deve digitar um valor maior que 5000! ')
    quit()

while count < tamanho : 
    listaNumeros.append(random.randint(0, 100))
    count+=1

def pesquisa(lista, item) :
    return lista.index(item)

valor = int(input('Digite o numero que deseja buscar: '))
print(f"O valor {valor} está presente na posição {pesquisa(listaNumeros, valor)}")


        


            









 
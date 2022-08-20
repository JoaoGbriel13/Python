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
    listaNumeros.append(random.randint(1, 100))
    count+=1

def buscar(lista) :
    buscar = int(input('Digite o numero que deseja encontrar: '))
    for i, item in enumerate(lista) :
        if item == buscar :
            print(f'Encontrado o valor {buscar} na posição {i}')
        if item == 0 :
            break
            

buscar(listaNumeros)




        


            









 
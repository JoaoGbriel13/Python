# Criando Lista e depois invertendo a ordem através do while loop, reverse, range e for
i = 0
li = []
while i < 10 :
    N = int(input('Digite os numeros: '))
    li.append(N)
    i = i + 1
    
print(li)
print('Invertendo...')

tamanho = len(li) - 1
newli = []

while (tamanho >= 0) :
    newli.append(li[tamanho])
    tamanho = tamanho - 1

rangelist = li[::-1]

reversedlist = list(reversed(li))

forli = [n for n in reversed(li)]

print(newli)
print(rangelist)
print(reversedlist)
print(forli)

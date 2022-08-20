min = int(input('Digite o numero entre 1 e 50 : '))
max = int(input('Digite o numero entre 1 e 50 : '))



lista = []

for i in range(min, max) :
    if i % 7 == 0 :
        lista.append(i)

print(lista)

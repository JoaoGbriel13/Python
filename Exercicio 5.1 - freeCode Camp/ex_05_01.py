count = 0 
valorTotal = 0


while True: 
    valorString = input('Digite os numeros: ')
    if valorString == 'done' or 'd':
        break
    try:
        valorFloat = float(valorString)
    except:
        print('Valor invalido!')
        continue
    count = count + 1
    valorTotal = valorFloat + valorTotal

print(f'O valor total é de {valorTotal}, a contagem é de {count} e a média é de {valorTotal/count}')




        
        




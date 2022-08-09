try :
    hours = float(input('Digite o numero de horas trabalhadas: '))
    rate = float(input('Digite o valor por hora recebido: '))

except : 
    hours = -1 
    rate = - 1
    if hours or rate < 0 :
        print(f'Você precisa digitar um numero válido!')
    quit()

if hours > 40 :
    extra = (hours - 40) * (rate * 0.5)
    pay = hours * rate + extra
    print(f'O pagamento é de : {pay}')
else :
    pay = hours * rate
    print(f'O pagamento é de : {pay}')


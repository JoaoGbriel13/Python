hours = float(input('Digite o numero de horas trabalhadas: '))
rate = float(input('Digite o valor por hora recebido: '))

if hours > 40 :
    extra = (hours - 40) * (rate * 0.5)
    pay = hours * rate + extra
    print(f'O pagamento é de : {pay}')
else :
    pay = hours * rate
    print(f'O pagamento é de : {pay}')


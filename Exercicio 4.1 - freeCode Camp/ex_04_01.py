def pagamento(hours, rate):
    if hours > 40 :
        print('Hora extra!')
        extra = (hours - 40) * (rate * 0.5)
        pay = hours * rate + extra
        print(f'O pagamento é de {pay}')
    else :
        print('Sem hora extra!')
        pay = hours * rate
        print(f'O pagamento é de : {pay}')

        
hours = float(input('Digite o numero de horas trabalhadas: '))
rate = float(input('Digite o valor por hora recebido: '))
pagamento(hours, rate)



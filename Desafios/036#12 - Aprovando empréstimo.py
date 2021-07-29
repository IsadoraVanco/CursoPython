casa = float(input('Qual o valor da casa a ser financiada?'))
salario = float(input('Quanto você recebe por mês?'))
anos = int(input('Por quantos anos você pretende pagar a casa?'))
mensal = casa/(anos*12)
if mensal>0.3*salario:
    print('Sua casa não poderá ser financiada, pois o valor mensal será maior que 30% de seu salário')
else:
    print('Empréstimo aceito. O valor mensal desta casa será de R${:.2f} por {:.0f} meses'.format(mensal,anos*12))


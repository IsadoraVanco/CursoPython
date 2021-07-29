salario = float(input('Qual é o salário do funcionário? R$'))
if salario >= 1250:
    aumento = salario + (salario*0.15)
else:
    aumento = salario + (salario*0.10)
print('O salário deste funcionário passará a ser de R${:.2f}'.format(aumento))

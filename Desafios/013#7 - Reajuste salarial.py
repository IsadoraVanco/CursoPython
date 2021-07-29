s = float(input('Qual o salário do funcionário?'))
a = s*0.15
ns = s+a
print('Um funcionário que ganhava R${}, com 15% de aumento(R${:.2f}), passa a receber R${:.2f}'.format(s,a,ns))

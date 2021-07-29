dias = int(input('Quantos dias com o carro alugado?'))
distancia = float(input('Quantos km foram percorridos com o carro?'))
t = dias*60.00 + distancia*0.15
print('O total a pagar é de R${:.2f}'.format(t))
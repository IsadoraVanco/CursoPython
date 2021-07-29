veloatual = float(input('Qual a velocidade atual do carro em km/h?'))
if veloatual>80:
    pagar = (veloatual-80)*7.00
    print('CUIDADO! Você ultrapassou o limite de velocidade(80km/h), por isso, será multado com R${:.2f}.'.format(pagar))
else:
    print('Sua velocidade está dentro do permitido. Tenha um bom dia!')

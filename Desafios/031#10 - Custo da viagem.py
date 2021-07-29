distancia = float(input('Qual é a distância em km da viagem?'))
if distancia>200:
    preco = distancia*0.45
 else:
    preco = distancia*0.5
print('Para esta viagem, você terá que pagar R${:.2f}'.format(preco))


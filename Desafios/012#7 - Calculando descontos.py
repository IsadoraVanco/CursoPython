p = float(input('Qual o preço do produto?'))
d = p*0.05
print('O produto que custava R${}, na promoção com o desconto de 5%(R${:.2f}) irá custar R${:.2f}'.format(p,d,p-d))

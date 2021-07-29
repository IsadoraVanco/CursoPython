print('-*' * 20)
print('MERCADÃO')
print('-*' * 20)
total = barato = caro = 0
produto = ''
nome = str(input('Produto:'))
produto = nome
preco = int(input('Preço: R$'))
barato = total = preco
if preco > 1000:
    caro = 1
escolha = str(input('Quer continuar? [S/N]')).strip().upper()
if escolha not in 'SN':
    escolha = str(input('Quer continuar? [S/N]')).strip().upper()
print('-*' * 20)
if escolha == 'S':
    while True:
        nome = str(input('Produto:'))
        preco = int(input('Preço: R$'))
        total += preco
        if preco > 1000:
            caro += 1
        if preco < barato:
            barato = preco
            produto = nome
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()
        if escolha not in 'SN':
            escolha = str(input('Quer continuar? [S/N]')).strip().upper()
        print('-*' * 20)
        if escolha == 'N':
            break
print('O total gasto nesta compra foi de R${:.2f}.'.format(total))
print('Foram comprados {} produtos mais caros que R$1000,00.'.format(caro))
print('O produto {} foi o mais barato, custando apenas R${:.2f}.'.format(produto, barato))

#solução do professor

'''total = barato = caro = contagem = 0
produto = ''
while True:
    nome = str(input('Produto:'))
    preco = int(input('Preço: R$'))
    contagem += 1
    total += preco
    if preco > 1000:
        caro += 1
    if contagem == 1 or preco < barato:
        barato = preco
        produto = nome
    resposta = ''
    while resposta not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper() [0]
    #[0] - apenas a primeira letra
    if resposta == 'N':
        break
print('O total gasto nesta compra foi de R${:.2f}.'.format(total))
print('Foram comprados {} produtos mais caros que R$1000,00.'.format(caro))
print('O produto {} foi o mais barato, custando apenas R${:.2f}.'.format(produto, barato))'''




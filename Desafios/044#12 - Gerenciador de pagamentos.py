preco = float(input('Preço das compras: R$'))
opcao = int(input('''OPÇÕES DE PAGAMENTO 
[1] Á vista no dinheiro ou cheque 
[2] Á vista no cartão 
[3] 2x no cartão 
[4] até 10x no cartão
Qual a opção?'''))
if opcao == 1:
    desconto = preco - (preco * 0.10)
    print('A sua compra de R${:.2f} terá um desconto de 10%, portanto, você pagará R${:.2f}.'.format(preco, desconto))
elif opcao == 2:
    desconto = preco - (preco * 0.05)
    print('A sua compra de R${:.2f} terá um desconto de 5%, portanto, você pagará R${:.2f}.'.format(preco, desconto))
elif opcao == 3:
    parcela = preco / 2
    print('A sua compra de R${:.2f} será parcelada em 2x sem juros no cartão. A parcela será de R${:.2f}.'.format(preco, parcela))
elif opcao == 4:
    juros = preco + (preco * 0.20)
    parcela = int(input('Em quantas vezes será realizada a parcela?'))
    print('A sua compra de R${:.2f} será parcelada em {}x no cartão. Você terá 20% de juros, contanto, passará a pagar o valor de R${:.2f} em {} parcelas, totalizando o valor de R${:.2f}.'.format(preco, parcela, juros / parcela, parcela, juros))
else:
    print('Esta opção não existe. Por favor, tente novamente.')
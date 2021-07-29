n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))
print('*-'*20)
print('Menu de opções:'
      '\n[1]somar'
      '\n[2]multiplicar'
      '\n[3]maior'
      '\n[4]novos números '
      '\n[5]sair do programa')
opcao = -1
while not opcao == 5:
    print('*-' * 20)
    opcao = int(input('>>>>>>>Ação desejada:'))
    if opcao == 1:
        print('A soma entre {} e {} resulta em {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('O resultado de {} x {} resulta em {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que {}'.format(n1,n2))
        elif n2 > n1:
            print('O número {} é maior que {}'.format(n2,n1))
        else:
            print('Os números são de mesmo valor')
    elif opcao == 4:
        print('Informe novamente os valores:')
        n1 = float(input('Qual o primeiro valor?'))
        n2 = float(input('Qual o segundo valor?'))
    else:
        print('Ação inválida. Tente novamente outro valor.')
from time import sleep
print('Encerrando...')
sleep(3)
print('Obrigada por usar o menu! Volte sempre!')


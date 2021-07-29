'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''
#trocando o while com uma condição por um 'while True' podemos criar um loop infinito
'''cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''
#usando o break em uma estrutura simples já realizada em exercicios
n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

#a partir da versão 3.6 do Python, foi atualizada uma maneira de formatar as strings
nome = 'Zé'
idade = 33
print('O {} tem {} anos.'.format(nome, idade))
#na versão mais nova, chamada 'f-string':(Python 3.6+)
print(f'O {nome} tem {idade} anos.')
#e numa versão mais antiga (Python 2)
print('O %s tem %d anos.'% (nome, idade))

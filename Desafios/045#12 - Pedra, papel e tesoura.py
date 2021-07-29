from random import choice
from time import sleep
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
if jogador > 2:
    print('Opção inválida. Tente novamente.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(1)
print('-*' * 10)
lista = ['PEDRA','PAPEL','TESOURA']
escolhido = choice(lista)
print('O computador escolheu {}'.format(escolhido))
if jogador == 0:
    print('Jogador escolheu PEDRA')
elif jogador == 1:
    print('Jogador escolheu PAPEL')
elif jogador == 2:
    print('Jogador escolheu TESOURA')
print('-*' * 10)
if escolhido == 'PEDRA' and jogador == 2 or escolhido == 'PAPEL' and jogador == 0 or escolhido == 'TESOURA' and jogador == 1:
    print('COMPUTADOR VENCEU')
elif escolhido == 'PEDRA' and jogador == 1 or escolhido == 'PAPEL' and jogador == 2 or escolhido == 'TESOURA' and jogador == 0:
    print('JOGADOR VENCEU')
else:
    print('EMPATE. Tente novamente.')


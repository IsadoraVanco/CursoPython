from random import randint
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10. \nSerá que você consegue adivinhar qual foi?')
n = randint(0, 10)
num = -1
tentativas = 0
while n != num:
    num = int(input('Qual o seu palpite?'))
    tentativas += 1
    if num > n:
        print('Menos...Tente mais uma vez.')
    elif num < n:
        print('Mais...Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))

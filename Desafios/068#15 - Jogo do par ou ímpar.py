print('*-' * 20)
print('PAR OU ÍMPAR')
print('*-' * 20)
from random import randint
total = vezes = 0
escolha = ''
while True:
    computador = randint(1, 10)
    jogador = int(input('Diga um valor de 0 á 10:'))
    if jogador > 10 or jogador < 0:
        print('Por favor, responda corretamente')
        jogador = int(input('Diga um valor de 0 á 10:'))
    escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    if escolha != 'P' and escolha != 'I':
        print('Por favor, responda corretamente.')
        escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    total = computador + jogador
    print('*-' * 20)
    print('Você jogou {} e o computador {}, portanto o total foi de {}.'.format(jogador, computador, total))
    print('->Par' if total % 2 == 0 else '->Ímpar')
    if total % 2 == 0 and escolha == 'P' or total % 2 == 1 and escolha == 'I':
        print('Você VENCEU!')
        vezes += 1
        print('-*' * 20)
        print('Vamos jogar novamente!')
        print('-*' * 20)
    else:
        print('Você PERDEU!')
        break
print('-*' * 20)
print('GAME OVER! Você venceu {} vezes.'.format(vezes))

#solução do professor

'''print('*-' * 20)
print('PAR OU ÍMPAR')
print('*-' * 20)
from random import randint
vezes = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Diga um valor de 0 á 10:'))
    total = jogador + computador 
    escolha = ''
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    print('*-' * 20)
    print('Você jogou {} e o computador {}, portanto o total foi de {}.'.format(jogador, computador, total))
    print('->Par' if total % 2 == 0 else '->Ímpar')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vezes += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vezes += 1
        else:
            print('Você PERDEU!')
            break
    print('-*' * 20)
        print('Vamos jogar novamente!')
        print('-*' * 20)
print('GAME OVER! Você venceu {} vezes.'.format(vezes))'''
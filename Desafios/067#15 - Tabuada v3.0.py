num = 0
while True:
    num = int(input('Qual o número para ver sua tabuada? [Digite um número negativo para finalisar o processo]'))
    print('-*' * 20)
    if num >= 0:
        for a in range(1,11):
            print('{} x {} = {}'.format(num, a, num * a))
    elif num < 0:
        break
    print('-*' * 20)
print('Programa encerrado. Volte sempre.')
# solução do professor
'''while True:
    num = int(input('Qual o número para ver sua tabuada? [Digite um número negativo para finalisar o processo]'))
    print('-*' * 20)
    if num < 0:
        break
    for a in range(1,11):
            print('{} x {} = {}'.format(num, a, num * a))
    print('-*' * 20)
print('Programa encerrado. Volte sempre.')
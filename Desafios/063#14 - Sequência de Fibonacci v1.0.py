print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
t = int(input('Quantos termos você quer mostrar?'))
print('-' * 20)
t1 = 0
t2 = 1
cont = 3
if t == 1:
    print('{} '.format(t1), end='')
elif t == 2:
    print('{} -> {} '.format(t1, t2), end='')
else:
    print('{} -> {}'.format(t1, t2), end='')
    while cont <= t:
        t3 = t1 + t2
        print(' -> {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        cont += 1
print(' -> Fim')

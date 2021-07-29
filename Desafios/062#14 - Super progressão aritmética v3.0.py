print('GERADOR DE P.A.')
print('*-' * 20)
p = int(input('Qual será o primeiro termo?'))
r = int(input('Qual será a razão?'))
contagem = 0
for A in range(0,10):
    print('{} -> '.format(p), end='')
    p += r
    contagem += 1
print('Pausa')
t = -1
while t != 0:
    t = int(input('Quantos termos você quer mostrar a mais?'))
    contagem += t
    if t != 0:
        for B in range(0,t):
            print('{} ->'.format(p), end=' ')
            p += r
        print('Pausa')
print('Progressão finalizada com {} termos mostrados.'.format(contagem))
#resolução do professor
'''p = int(input('Primeiro termo:'))
r = int(input('Razão da PA'))
t = p
c = 1
t =0
mais = 10
while mais != 0:
    t += mais
    while c <= t:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
    print('Progressão finalizada com {} termos mostrados'.format(t))'''

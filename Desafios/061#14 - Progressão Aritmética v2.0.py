print('GERADOR DE P.A.')
print('*-' * 20)
p = int(input('Qual será o primeiro termo da Progressão Aritmética?'))
r = int(input('Qual será a razão?'))
a10 = p + 9 * r
v = p
while v != a10:
    print('{} -> '.format(v), end='')
    v += r
print('{} -> FIM!'.format(a10))


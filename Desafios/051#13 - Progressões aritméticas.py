p = int(input('Qual o primeiro termo?'))
r = int(input('Qual a razão?'))
d = p + (10 -1) * r
for c in range(p,d + r,r):
    print(c, end='->')
print('FIM')


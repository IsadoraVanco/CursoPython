n = int(input('Digite um número:'))
s = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[36m', end=' ')
        s += 1
    else:
        print('\033[30m', end=' ')
    print(c, end=' ')

print('\n\033[mO número {} foi divisível {} vezes'.format(n,s))
if s == 2:
    print('E por isso ele não é um número primo!')
else:
    print('E este número é um número primo!')

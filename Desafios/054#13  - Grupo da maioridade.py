from datetime import date
ano = date.today().year
maior = ano - 18
ma = 0
me = 0
for c in range(1,8):
    i = int(input('Digite o ano de nascimento da {}ª pessoa:'.format(c)))
    if i <= maior :
        ma += 1
    else:
        me += 1
print('Entre essas pessoas, há {} que são maiores de idade e {} menores de idade'.format(ma,me))


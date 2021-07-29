from datetime import date
ano = int(input('Ano de nascimento:'))
idade = date.today().year - ano
print('O atleta nascido em {}, hoje tem {} anos'.format(ano, idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')


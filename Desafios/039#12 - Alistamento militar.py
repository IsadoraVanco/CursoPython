from datetime import date
nasc = int(input('Ano de nascimento:'))
idade = date.today().year - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, date.today().year))
if idade < 17:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(date.today().year + saldo))
elif idade == 17:
    print('Ainda falta 1 ano para o alistamento')
    print('Seu alistamento será em {}'.format(date.today().year + 1))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade == 19:
    print('Você deveria ter se alistado há 1 ano.')
    print('Seu alistamento foi em {}.'.format(date.today().year - 1))
elif idade > 19:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(date.today().year - saldo))


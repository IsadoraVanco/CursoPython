media = 0
hv = 0
hn = ''
m = 0
for teste in range(1,5):
    print('*** {}ª Pessoa ***'.format(teste))
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    media += idade
    if teste == 1:
        if sexo == 'M':
            hv = idade
            hn = nome
        elif sexo == 'F' and idade < 20:
            m += 1
    else:
        if sexo == 'M' and idade > hv:
            hv = idade
            hn = nome
        elif sexo == 'F' and idade < 20:
            m += 1
print('A média de idade do grupo é de {:.2f} anos'.format(media/4))
print('O homem mais velho tem {} anos e se chama {}'.format(hv,hn))
print('Ao todo são 2 mulheres com menos de 20 anos'.format(m))


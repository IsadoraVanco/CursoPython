print('\033[1;30;46mOlá, mundo!\033[m')
print('\033[32mIsto é apenas um teste de cor\033[m')
nome = 'Isa'
print('Olá, {}{}{}...'.format('\033[1;33;45m',nome, '\033[m'))
cores = {'limpa':'\033[m',
         'pretoebranco':'\033[7;30m'}
print('Nesta frase usarei o preto e branco,{}{}{}'.format(cores['pretoebranco'],nome,cores['limpa']))
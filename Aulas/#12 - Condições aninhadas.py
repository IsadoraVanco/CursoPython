nome = str(input('Qual o seu nome?')).strip().capitalize()
if nome == 'Isadora':
    print('Olá {},Que belo nome!'.format(nome))
elif nome == 'Paulo' or nome == 'Pedro' or nome == 'Maria' or nome == 'Ana' or nome == 'João':
    print('Olá {}, Seu nome é popular no Brasil!'.format(nome))
elif nome in 'Mariana Manuela Marcos Emanuel':
    print('Olá {}, Que nome bonito!'.format(nome))
else:
    print('Olá {}, Seu nome é tão comum'.format(nome))
print('Tenha um bom dia!')

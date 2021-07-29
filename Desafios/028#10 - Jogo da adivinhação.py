#pode-se usar 'randint(0,5)'
from random import choice
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = choice([0,1,2,3,4,5])
numero = int(input('Em que número pensei?'))
print('Processando...')
sleep(3)
if num == numero:
    print('Parabéns! Você acertou! O número que pensei foi {}'.format(num))
else:
    print('Oops! Não foi dessa vez, o número que eu escolhi foi {}. Mais sorte da próxima vez.'.format(num))

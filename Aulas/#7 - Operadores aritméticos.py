#Operadores Aritméticos
print('Exercício 01')
nome = str(input('Qual o seu nome?'))
#podemos usar sinais como < > ^ (alinhamentos) após um : para alterarmos a forma como será exibido o texto.
print('Prazer em te conhecer {}!'.format(nome))
print('Agora com modificações em 20 espaços:o nome .{:20}.'.format(nome))
print('O nome .{:>20}. com variação ">"'.format(nome))
print('variação "<":.{:<20}.'.format(nome))
print('E mais "*^":.{:*^20}.'.format(nome))
print('Exercício 02')
n1 = int(input('Um valor'))
n2 = int(input('Outro'))
s = n1+n2
m = n1*n2
d = n1/n2
su = n1-n2
di = n1//n2
p = n1**n2
r = n1%n2
print('Com estes valores, a soma vale {},\n a multiplicação {},\n a subtração {},\n e a exponenciação {}.\n A divisão resulta em {:.2f},'.format(s,m,su,p,d), end=' ')
print('contanto, o resto da divisão é {}, e a divisão inteira vale {}'.format(r,di))
#.2f significa no máximo duas casas flutuantes, ou seja, depois da vírgula
#\n significa "nova linha" e se colocarmos um "end='algo/nada'" podemos continuar a linha com o comando debaixo
print('********DESAFIO 005**********')
n = int(input('Um Número'))
n2 = n -1
n3 = n +1
print('Seu número é {}, porém,antes dele, vêm o {} e depois dele, vêm o {}'.format(n,n2,n3))
print('********DESAFIO 006**********')
n = int(input('Número'))
n2 = n*2
n3 = n*3
n4 = n**(1/2)
print('Seu dobro é {}, o triplo {} e sua raiz quadrada é {:.2f}'.format(n2,n3,n4))
print('********DESAFIO 007***********')
print('Um aluno tirou duas notas diferentes em dois semestres, decida-se quais serão as suas notas e vamos calcular a sua média')
n = int(input('primeira nota'))
n2 = int(input('a segunda nota'))
n3 = (n+n2)/2
print('A nota média deste aluno foi de {}'.format(n3))
print('*********DESAFIO 008**********')
M = float(input('Uma quantidade em metros'))
c = M*100
m = M*1000
print('Em {:.2f}m, temos {:.2f}cm, e {:.2f}mm'.format(M,c,m))
print('*********DESAFIO 009***********')
n = int(input('Qualquer número'))
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
#Até o 5 já está bom, não é mesmo?
print('{}*1={}\n{}*2={}\n{}*3={}\n{}*4={}\n{}*5={}'.format(n,n,n,n2,n,n3,n,n4,n,n5))
print('********DESAFIO 010***********')
r = float(input('Quantos Reais você tem na carteira?'))
d = r//3.27
print('Com esses {:.2f} reais, você pode ter {:.2f} dólares'.format(r,d))
print('********DESAFIO 011************')
print('Preciso que você me ajude á decidir o tamanho de uma parede. Por favor, diga para mim,')
a = float(input('Qual será a sua altura em metros?'))
l = float(input('E a sua largura?'))
ap = a*l
t = ap /2**2
print('Esta parede tem uma área de {:.2f} m2.\nUm litro de tinta consegue pintar 4m2,\nentão, precisaremos de {} lts desta tinta para pintarmos esta parede'.format(ap,t))
print('**********DESAFIO 012***********')
print('Uma loja está fazendo uma promoção de qualquer produto com 5% de desconto, por favor, diga para mim,')
p = float(input('Qual o valor do produto pelo o qual você se interessou?'))
d = p*5/100
v = p-d
print('O seu produto terá um desconto de {:.2f} reais, portanto, na promoção, ele custará {:.2f} reais '.format(d,v))
print('**********DESAFIO 013***********')
print('Você trabalha em uma empresa onde você se dá muito bem, e a cada dia progride cada vez mais.\n Seu chefe irá te promover e você terá 15% de aumento em seu salário a partir do mês que vem. ')
s = float(input('Diga-me, quanto você ganha por mês?'))
a = s*0.15
n = s + a
print('Você terá um aumento de {:.2f} reais, e passará a receber {:.2f} reais'.format(a,n))
print('Acabamos. UFA!')
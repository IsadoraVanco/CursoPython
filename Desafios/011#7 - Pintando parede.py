l = float(input('Qual a largura da parede?'))
al = float(input('E a altura?'))
a = al*l
t = a/2
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {} metros quadrados.'.format(l,al,a))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(t))

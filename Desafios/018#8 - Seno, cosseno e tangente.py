from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tang))

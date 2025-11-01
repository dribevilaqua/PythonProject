import math

ca = float(input('Qual cateto adjacente:'))
co = float(input('Qual cateto oposto?:'))
h = math.sqrt((ca**2)+(co**2))
print('Nesse triânculo retangulo a hipotenusa vale: {:.2f}'.format(h))

#agora com o python fazendo com formula da hipotenusa

ca = float(input('Qual cateto adjacente:'))
co = float(input('Qual cateto oposto?:'))
h = math.hypot(ca, co)
print('Nesse triânculo retangulo a hipotenusa vale: {:.2f}'.format(h))




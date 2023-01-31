#Programa que leia um ângulo, calcule e mostre seu seno,cosseno e tangente
# importado da bilbioteca .math OBS: precisa ser em radianos

import math
ang = float(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(' Seno de {} = {:.2f}\n Cosseno de {} = {:.2f}\n Tangente de {} = {:.2f}'.format(ang,sen,ang,cos,ang,tan) )

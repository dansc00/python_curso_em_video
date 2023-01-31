#Programa que leia o comprimento do cateto oposto e adjacente de um triângulo retângulo
# e mostre o valor da hipotenusa
# Lembrete: Teorema de pitágoras, hip²= catop² + catadj²
import math
catop = float(input('Digite o comprimento do cateto oposto do triângulo(em M): '))
catadj = float(input('Digite o comprimento do cateto adjacente do triângulo(em M): '))
somacats = (catop**2 + catadj**2)
hip = math.sqrt(somacats)
print('A hipotenusa do triângulo retângulo vale {:.2f}M'.format(hip))
#Poderia usar também o comando da biblioteca math hypot(x,y)

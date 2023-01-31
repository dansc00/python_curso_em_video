#Programa que leia um número real e mostre sua parte inteira
#Nota: truncar = passar de real para inteiro
import math
val = float(input('Digite um número real qualquer: '))
valint = math.trunc(val)
print('A parte inteira do valor {} é {}'.format(val,valint))




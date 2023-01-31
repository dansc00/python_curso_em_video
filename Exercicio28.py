# Programa que leia um número e diga se ele é par ou ímpar

num = int(input('Digite um número: '))
teste = num % 2 #Resto da divisão inteira por 2, se sobrar é impar se for 0 é par
if teste == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))
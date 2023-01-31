#Programa que leia um número de 0 a 9999 e mostre cada um dos digitos separados
#Divida em unidade,dezena,centena,milhar

# Número em formato string
num = str(input('Digite um número de 0 até 9999: '))
print('Valores de: ')
print('Unidade = {}'.format(num[3]))
print('Dezena = {}'.format(num[2]))
print('Centena = {}'.format(num[1]))
print('Milhar = {}'.format(num[0]))





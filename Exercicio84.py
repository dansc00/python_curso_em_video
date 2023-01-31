# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random
num1 = random.randint(1,100)
num2 = random.randint(1,100)
num3 = random.randint(1,100)
num4 = random.randint(1,100)
num5 = random.randint(1,100)
tupla = (num1,num2,num3,num4,num5)
print(f'TUPLA = {tupla}')
print(f'Maior valor = {max(tupla)}')
print(f'Menor valor = {min(tupla)}')



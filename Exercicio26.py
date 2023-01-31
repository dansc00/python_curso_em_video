# Programa que sorteie um número inteiro entre 0 e 5 e peça para o usuário tentar
# advinhar qual é este número, exiba se o usuário venceu ou perdeu

import random
from time import sleep
nums = [0,1,2,3,4,5]
val1 = random.choice(nums)
print('PC pensa em um número entre 0 e 5...')
sleep(2) #Faz o código parar 4 segundos
print('Escolhido! Tente advinhar qual número o PC pensou :)')
val2 = int(input('Digite um número entre 0 e 5: '))
if val2 == val1:
    print('Parabéns! você acertou,o número escolhido foi {}'.format(val1))
else:
    print('Que pena, você errou,o número escolhido foi {}'.format(val1))
#Poderia ter usado o .randint do random, sortearia um número inteiro de (x, y)
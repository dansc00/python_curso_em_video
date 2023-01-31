# Programa que mostre na tela a contagem para o inicio de uma queima de fogos
# com uma contagem regressiva de 10 a 0 e com um intervalo de 1 segundo entre eles

from time import sleep
inicio = str(input('\033[1;31mDigite X para iniciar a queima de fogos.').upper().strip())
if inicio == 'X':
    for x in range(10,-1,-1):
        print(x)
        sleep(1)
    print('COMEÇARAM OS FOGOS!')
else:
    print('Talvez outra hora.')


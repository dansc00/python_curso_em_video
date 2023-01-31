# Programa que leia um número inteiro e diga se ele é ou não número primo

val = int(input('Digite um valor: '))
total = 0
print('\033[1;31mVERMELHO - DIVISÍVEIS')
print('\033[1;33mAMARELO - NÃO DIVISÍVEIS')
for x in range(1,val+1):
    if val % x == 0:
        print('\033[31m', end='')
        total = total + 1
    else:
        print('\033[33m', end='')
    print('{}\033[m'.format(x), end=' ')
if total == 2:
    print('\nO número {} É PRIMO'.format(val))
else:
    print('\nO número {} NÃO É PRIMO'.format(val))




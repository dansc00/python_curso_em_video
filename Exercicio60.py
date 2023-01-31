# Programa que leia um numero n inteiro e mostre na tela os n primeiros elementos de uma
# SEQUÊNCIA DE FIBONACCI

cont = 2
seta = '-->'
seqi = 1
var = 1
result = 0
print('\033[1;32m#'*10+' \033[1;36mSEQUÊNCIA DE FIBONACCI '+'\033[1;32m#'*10)
print('')
n = int(input('\033[1;36mDigite o total de elementos da SEQUÊNCIA DE FIBONACCI que deseja ver: '))
if n == 1:
    print('\033[1;33m1 {} '.format(seta),end='')
elif n == 2:
    print('\033[1;33m1 {} 1 {} '.format(seta, seta),end='')
elif n > 2:
    print('\033[1;33m1 {} 1 {} '.format(seta, seta), end='')
    while cont!=n:
        result = seqi + var
        cont += 1
        print(result,end='')
        print(' --> ',end='')
        seqi = var
        var = result
print('FIM')








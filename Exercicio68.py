# Programa que simule o funcionamento de um caixa eletrônico. Pergunte ao usuário:
# Qual será o valor sacado(número inteiro) e o programa informa quantas cédulas de cada
# valor serão entregues.
# CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE :R$50 R$20 R$10 E R$1

print('\033[1;31m{:^60}'.format(' BANCO ONLINE - CAIXA ELETRÔNICO '))
print('')
val = int(input('\033[;30mDigite o total que deseja sacar(EM R$, DESCONSIDERE CENTAVOS): R$'))
total = val
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'\033[1;33m[{totced} CÉDULA(S) DE R${ced}]')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break





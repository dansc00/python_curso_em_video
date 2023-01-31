# Programa que jogue par ou ímpar com o usuário, o programa deve ser interrompido quando
# o jogador perder, mostrando o total de vitórias conquistadas

import random
from time import sleep
player = pc = ''
contv = nump = numpc = final = 0
print('\033[1;30m#'*20+' \033[1;31mPAR OU ÍMPAR '+'\033[1;30m#'*20)
print('')
print('\033[1;32m[SISTEMA]Você jogará par ou ímpar com o pc!')
opcao = str(input('[SISTEMA]Pronto para começar? Digite x(outra letra para sair): ').strip().upper())
print('')
if opcao == 'X':
    while True:
        player = str(input('\033[1;32m[SISTEMA]Escolha sua jogada, par ou ímpar?(P/I): ').strip().upper())
        nump = int(input('[SISTEMA]Jogue um número entre 0 e 100: '))
        print('\033[1;30mPC ESCOLHENDO...')
        sleep(2)
        pc = random.choice('PI')
        numpc = random.randint(0,100)
        final = numpc + nump
        if (player == 'P' or player == 'I') and (nump <= 100 and nump >=  0):
            if player == 'P' and final % 2 != 0 or player == 'I' and final % 2 == 0:
                break
            elif player == 'P' and final % 2 == 0:
                print(f'\033[1;32mPLAYER JOGA {nump}, PC JOGA {numpc}')
                print(f'O RESULTADO FOI {final}(PAR), PARABÉNS VOCÊ VENCEU!')
                contv += 1
                print('\033[1;30mVOLTANDO AO INÍCIO... ')
                print('-' * 40)
                sleep(2)
            elif player == 'I' and final % 2 != 0:
                print(f'\033[1;32mPLAYER JOGA {nump}, PC JOGA {numpc}')
                print(f'O RESULTADO FOI {final}(ÍMPAR), PARABÉNS VOCÊ VENCEU!')
                contv += 1
                print('\033[1;30mVOLTANDO AO INÍCIO... ')
                print('-' * 40)
                sleep(2)
        else:
            print('\033[1;31mINVÁLIDO, SIGA AS INSTRUÇÕES DADAS!')
            print('TENTE NOVAMENTE')
            print('\033[1;30mVOLTANDO AO INÍCIO... ')
            print('-' * 40)
            sleep(2)
    if player == 'P':
        print(f'\033[1;31mPLAYER JOGA {nump}, PC JOGA {numpc}')
        print(f'O RESULTADO FOI {final}(ÍMPAR), QUE PENA VOCÊ PERDEU!')
        print('\033[1;30mCALCULANDO RESULTADO...')
        sleep(2)
    elif player == 'I':
        print(f'\033[1;31mPLAYER JOGA {nump}, PC JOGA {numpc}')
        print(f'O RESULTADO FOI {final}(PAR), QUE PENA VOCÊ PERDEU!')
        print('\033[1;30mCALCULANDO RESULTADO...')
        sleep(2)
    print(f'\033[1;32m[SISTEMA]Você conseguiu ao todo {contv} vitórias')
else:
    print('\033[1;32m[SISTEMA]Que pena! talvez outra hora')

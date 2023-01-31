# Melhora desafio 28: PC pensará em um número entre 0 e 10, porém agora o jogador
# vai tentar advinhar até acertar, mostrando no fim quantos palpites foram necessários
# para vencer

from time import sleep
import random
lista = [1,2,3,4,5,6,7,8,9,10]
player = 0
print('\033[1;30m-=-'*10)
print('\033[1;31m     JOGO DA ADVINHAÇÃO')
print('\033[1;30m-=-'*10)
print('')
print('\033[1;32m[SISTEMA]O PC pensará em um número entre 0 e 10 e você tentará advinhar')
print('')
teste = str(input('\033[1;31m[PC]Está pronto? Digite X para iniciar: ').upper().strip())
if teste == 'X':
    print('\033[1;31m[PC]Vamos lá!')
    print('[PC]Pensando...')
    sleep(2)
    print('')
    pc = random.choice(lista)
    while player != pc:
        player = int(input('\033[1;32m[SISTEMA]Tente acertar em que número o PC pensou: '))
        print('')
        if player != pc:
            print('\033[1;32m[SISTEMA]Você errou, tente novamente')
    print('\033[1;32m[SISTEMA]Parabéns, o PC realmente pensou no número {}'.format(player))
else:
    print('\033[1;31m[PC]Tudo bem, talvez outra hora')






# Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

# Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

# Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

# Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

# Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa"

# Caso contrário, o computador toma a inciativa de começar o jogo.

# Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

# Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

import random
from time import sleep

def computador_escolhe_jogada(x,y):
        aux = random.randint(1,y)
        while True:
            if (x - aux)%(y+1)== 0:
                x -= aux
                return x
            break

def partida():
    n = 21
    while n > 20:
        n = int(input('Com quantas peças você deseja jogar?(Máximo de 20 peças): '))
        if n > 20:
            print('O NÚMERO DE PEÇAS NÃO PODE EXCEDER O TOTAL DE 20. TENTE NOVAMENTE')
            print()
    m = n
    while m >= n:
        m = int(input('Máximo de peças que poderão ser retiradas por rodada(Número menor que o máximo de peças): '))
        if m >= n:
            print('NÚMERO MAIOR OU IGUAL AO MÁXIMO DE PEÇAS. TENTE NOVAMENTE')
            print()
    if n % (m+1) == 0:
        print('Sorteando quem iniciará o jogo...')
        sleep(2)
        print(f'Player começa!')

        print(computador_escolhe_jogada(n,m))








partida()





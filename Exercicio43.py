# Programa que faça o PC jogar pedra, papel, tesoura com o usuário

from time import sleep
import random
print('\033[1;31;m-=-'*30)
print('\033[1;32;m                              PEDRA,PAPEL,TESOURA!!! :)')
print('\033[1;31;m-=-'*30)
print(''' 
              __     __                                  _  _
              \  \  /  /           _____              _ | || |
               \  \/  /           | | | |            | || || |                                   
               | \  / |           | | | |            | || || |                                    
               \     /            \     /            \      /                     
                /   |             /    |             /     |                     
               /    |            /     |            /      |               
              /     |           /      |           /       |            
             /      |          /       |          /        |                  
                                                                  ''')
print('')
opcao = str(input('\033[;31m[PC]OLÁ, EU SOU O PC, VAMOS JOGAR O FAMOSO JOGO JOKENPÔ OU PEDRA, PAPEL E TESOURA?(S/N)').upper().strip())
if opcao == 'S':
    print('')
    print('''[PC]VOU TE EXPLICAR AS REGRAS:
    HAVERÁ TRÊS OPÇÕES(1,2,3) SEQUENCIALMENTE IGUAIS À PEDRA,PAPEL,TESOURA
    QUANDO EU ANUNCIAR VALENDO, HAVERÁ A CONTAGEM JO,KEN,PÔ. NESSE MOMENTO VOCÊ ESCOLHE 
    SUA JOGADA.''')
    sleep(6)
    print('[PC]VAMOS LÁ ENTÃO.')
    opcao2 = str(input('\033[1;32m[SISTEMA]TECLE X QUANDO ESTIVER PRONTO.').upper().strip())
    sleep(2)
    if opcao2 == 'X':
        print('\033[1;32m3...')
        sleep(2)
        print('2...')
        sleep(2)
        print('1...')
        sleep(1)
        print('VALENDO!')
        print('')
        print('JO...')
        sleep(2)
        print('KEN...')
        sleep(2)
        print('PÔ!')
        sleep(1)
        print('')
        lista = [1,2,3]
        pc = random.choice(lista)
        print('[1]PEDRA')
        print('[2]PAPEL')
        print('[3]TESOURA')
        player = int(input('[SISTEMA]FAÇA SUA ESCOLHA: '))
        print('')
        print('[SISTEMA]PLAYER ESCOLHE {}, PC ESCOLHE {}.'.format(player,pc))
        if player == 1 and pc == 2:
            print('\033[;31m[PC]HAHAHA! EU TE VENCI!')
        elif player == 1 and pc == 3:
            print('[PC]OH NÃO! VOCÊ ME VENCEU!')
        elif player == 2 and pc == 1:
            print('[PC]OH NÃO! VOCÊ ME VENCEU!')
        elif player == 2 and pc == 3:
            print('[PC]HAHAHA! EU TE VENCI!')
        elif player == 3 and pc == 1:
            print('[PC]HAHAHA! EU TE VENCI!')
        elif player == 3 and pc == 2:
            print('[PC]OH NÃO! VOCÊ ME VENCEU!')
        elif player == 1 and pc == 1 or player == 2 and pc == 2 or player == 3 and pc == 3:
            print('[PC]EMPATAMOS! HEHE')
        elif player < 1 or player > 3:
            print('\033[1;32m[SISTEMA]COMANDO INVÁLIDO! TENTE NOVAMENTE')
else:
    print('\033[;31m[PC]QUE PENA, TALVEZ OUTRA HORA')











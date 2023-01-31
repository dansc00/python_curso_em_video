# Crie um programa que leia dois valores e mostre um menu na tela:
# 1 para somar
# 2 para multiplicar
# 3 mostra o maior
# mudar os números
# sair do programa

from time import sleep
opcao = 0
val1 = float(input('Digite o primeiro valor: '))
val2 = float(input('Digite o segundo valor: '))
print('')
while opcao!= 5:
    print('\033[1;30m*'*30)
    print('     \033[1;34m      MENU')
    print('\033[1;30m*'*30)
    print('''\033[34m    [1]Somar Números
    [2]Multiplicar Números
    [3]Mostar o maior número
    [4]Trocar números
    [5]Sair''')
    print('')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        soma = val1 + val2
        print('A SOMA entre {} e {} é igual a {}'.format(val1,val2,soma))
        print('VOLTANDO AO MENU EM...')
        sleep(2)
        for x in range(1,4):
            print(x)
            sleep(1)
    elif opcao == 2:
        produto = val1 * val2
        print('O PRODUTO de {} por {} é igual a {}'.format(val1,val2,produto))
        print('VOLTANDO AO MENU EM...')
        sleep(2)
        for x in range(1,4):
            print(x)
            sleep(1)
        sleep(1)
    elif opcao == 3:
        if val1 > val2:
            print('{} é MAIOR que {}'.format(val1,val2))
            print('VOLTANDO AO MENU EM...')
            sleep(2)
            for x in range(1,4):
                print(x)
                sleep(1)
        else:
            print('{} é MAIOR que {}'.format(val2,val1))
            print('VOLTANDO AO MENU EM...')
            sleep(2)
            for x in range(1,4):
                print(x)
                sleep(1)
    elif opcao == 4:
        val1 = float(input('Digite novamente o primeiro valor: '))
        val2 = float(input('Digite novamente o segundo valor: '))
        sleep(1)
        print('VOLTANDO AO MENU EM...')
        for x in range(1,4):
            print(x)
            sleep(1)
    elif opcao!=1 and opcao!=2 and opcao!=3 and opcao!=4 and opcao!=5:
        print('POR FAVOR, ESCOLHA APENAS AS OPÇÕES PRESENTES NO MENU')
        print('TENTE NOVAMENTE')
        print('VOLTANDO AO MENU EM...')
        sleep(1)
        for x in range(1,4):
            print(x)
            sleep(1)
print('\033[1;31mPROCESSO FINALIZADO')

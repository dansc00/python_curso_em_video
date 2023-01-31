# Programa que diga o valor que será pago por um produto, considerando seu preço normal
# e condições de pagamento:
# À vista: dinheiro/cheque = 10% de desconto
# A vista no cartão: 5% de desconto
# Em até 2x no cartão = preço normal
# 3x ou mais no cartão = 20% de juros
from time import sleep
print('\033[1;32m-$'*20)
print('\033[1;33m  BEM VINDO AO SISTEMA DE PAGAMENTOS')
print('\033[1;32m-$'*20)
prod = float(input('\033[;34mDigite o valor do produto(em R$): R$'))
print('''ESCOLHA UMA DAS OPÇÕES DE PAGAMENTO ABAIXO:
1- À VISTA NO DINHEIRO OU CHEQUE
2- À VISTA NO CARTÃO
3- PARCELADO NO CARTÃO''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('VOCÊ ESCOLHEU O PAGAMENTO À VISTA NO DINHEIRO OU CHEQUE!')
    print('Receberá 10% de desconto no produto')
    print('Aguarde...')
    sleep(3)
    desc = (prod * 10)/100
    valf = prod - desc
    print('Valor final do produto = R${:.2f}'.format(valf))
elif opcao == 2:
    print('VOCÊ ESCOLHEU O PAGAMENTO À VISTA NO CARTÃO')
    print('Receberá 5% de desconto no produto')
    print('Aguarde...')
    sleep(3)
    desc = (prod * 5)/100
    valf = prod - desc
    print('Valor final do produto = R${:.2f}'.format(valf))
elif opcao == 3:
    print('VOCÊ ESCOLHEU PAGAR PARCELADO NO CARTÃO')
    parc = int(input('Em quantas vezes pretende parcelar o produto(A partir de 2x): '))
    if parc == 2:
        print('Você escolheu pagar em até 2x no cartão')
        print('Não receberá descontos')
        print('Aguarde...')
        sleep(3)
        print('Valor final = R${:.2f}'.format(prod))
    elif parc >= 3:
        print('Você escolheu pagar em até {}x no cartão'.format(parc))
        print('Será acrescentado um valor de 20% em juros')
        print('Aguarde...')
        sleep(3)
        juros = (prod * 20)/100
        valf = prod + juros
        print('Valor final do produto = R${:.2f}'.format(valf))
    elif parc <= 1:
        print('\033[1;31mESSA OPÇÃO DE PARCELA É INEXISTENTE, TENTE NOVAMENTE')


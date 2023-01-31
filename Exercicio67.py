# Programa que leia o nome e preço de vários produtos, pergunte se o usuário quer continuar.
# Mostre no final: O total gasto,Qnts produtos custam mais de R$1000,00 e
# o nome do produto mais barato

cont = tot = prod1k = prodbar = 0
nprodbar = ''
print('\033[1;33m{:$^50}'.format(' MERCADO ONLINE '))
print('')
while True:
    cont += 1
    nprod = str(input(f'\033[;32mDigite o nome do {cont}º produto: ').strip().upper())
    rprod = float(input(f'Digite o preço do {cont}º produto(em R$): R$'))
    opcao = ' '
    tot += rprod
    if rprod > 1000.00:
        prod1k += 1
    if cont == 1:
        prodbar = rprod
        nprodbar = nprod
    elif rprod < prodbar:
        prodbar = rprod
        nprodbar = nprod
    while opcao not in 'SN':
        opcao = str(input('Deseja adicionar mais produtos?[S/N]: ').strip().upper()[0])
        if opcao not in 'SN':
            print('\033[1;31mDIGITE APENAS S para SIM ou N para NÃO')
            print('TENTE NOVAMENTE')
    print('\033[1;30m~' * 50)
    if opcao == 'N':
        break
print(f'\033[1;32mTOTAL GASTO = R${tot:.2f}')
print(f'{prod1k} PRODUTOS CUSTAM MAIS DE R$1000,00')
print(f'O PRODUTO MAIS BARATO É O(A) {nprodbar}, CUSTANDO R${prodbar:.2f}')

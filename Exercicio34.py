# Programa que aprove um empréstimo para compra de casa, pergunte:
# O valor da casa, o salário do comprador e em quantos anos ele irá pagar
# Calcule o valor da prestação mensal. Ela não pode exceder 30% do salário
# Nesse caso o empréstimo é negado

print('\033[0;34m-=-'*10)
print('\033[1;33mBEM VINDO AO SISTEMA DE COMPRA!')
print('\033[0;34m-=-'*10)
print('')
valcasa = float(input('\033[;33mDigite o valor que custará a casa(em reais): R$'))
sal = float(input('Digite o valor de seu salário atual(em reais): R$'))
anos = int(input('Digite em quantos anos irá pagar o imóvel:\033[m '))
totalmeses = anos * 12
prestação = valcasa / totalmeses
if prestação <= (sal*30)/100:
    print('\033[1;32m O empréstimo foi aprovado!')
    print('\033[;33m Valor da prestação = {}X de R${:.2f}'.format(totalmeses,prestação))
else:
    print('\033[1;31m O empréstimo foi negado!')
    print('\033[;33m O valor da prestação está acima de 30% de seu salário -> ',end='')
    print('Valor da prestação = {}X de {:.2f}'.format(totalmeses,prestação))


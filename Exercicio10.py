# Crie um programa que leia quanto de dinheiro uma pessoa possui na carteira
# e mostre quantos dólares ela pode comprar. Considere: US$1,00 = R$3,27

rs = (float(input('Digite quantos reais a pessoa possui: R$')))
us = (rs/3.27)
print('Com R${:.2f}(reais) a pessoa poderá comprar aproximadamente U${:.2f}(dólares)'.format(rs,us))
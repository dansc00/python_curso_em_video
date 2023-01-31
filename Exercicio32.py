# Programa que calcule um salário e mostre o valor do aumento
# Para salários acima de de R$1250,00 aumento de 10%
# Para inferiores ou iguais aumento de  15%
from time import sleep
sal = float(input('Digite o valor do salário(em reais): R$'))
print('Analisando valor do aumento e salário novo...')
sleep(2)
if sal>1250:
    aumento = (sal*10)/100
else:
    aumento = (sal*15)/100
sal2 = (sal + aumento)
print('Valor do aumento = R${:.2f}'.format(aumento))
print('Salário novo = R${:.2f}'.format(sal2))
# Programa que pergunte a distância de uma viagem em KM e calcule o preço da passagem
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

from time import sleep
dist = float(input('Digite a distância da viagem(Em Km): '))
print('Calculando preço da passagem. Aguarde...')
sleep(2)
if dist <= 200:
    preço = (dist * 0.50)
else:
    preço = (dist * 0.45)
print('A passagem custará R${:.2f}'.format(preço))

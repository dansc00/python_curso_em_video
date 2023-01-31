# Programa que leia a velocidade de um carro, se ele ultrapassar 80 km/h
# Exiba uma mensagem dizendo q ele foi multado, a multa custará R$7,00 por cada km acima.

from time import sleep
vel = float(input('Velocidade do carro(em Km/H): '))
multa = (vel - 80) * 7.00
if vel > 80:
    print('VEÍCULO ULTRAPASSOU O lIMITE DE 80Km/h!!!')
    print('SERÁ APLICADO UMA MULTA, AGUARDE O CÁLCULO DO VALOR...')
    sleep(3)
    print('Valor da multa = R${:.2f}'.format(multa))
else:
    print('Velocidade dentro do limite de 80Km/H. Siga a viagem.')
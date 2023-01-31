# Programa que leia o primeiro termo e a razão de uma PA e mostre os 10 primeiros termos
# dessa progressão


termo = int(input('Digite o valor do primeiro termo da PA: '))
razao = int(input('Digite o valor da razão da PA: '))
print('10 PRIMEIROS TERMOS DA PA:')
for x in range(termo, termo+10*razao ,razao):
    print(x,end=',')





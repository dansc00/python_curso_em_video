# Programa que leia o peso de cinco pessoas e mostre qual foi o maior e menor peso lido

pesos = [1,2,3,4,5]
maior = 0
menor = 0
for x in range(1,6):
    pesos[x-1] = float(input('Digite o peso da {}ª pessoa: '.format(x)))
maior = max(pesos)
menor = min(pesos)
print('O MAIOR peso lido foi de {:.1f} Kg e o MENOR foi {:.1f} Kg'.format(maior,menor))













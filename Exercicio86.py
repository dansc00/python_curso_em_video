# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = ('Arroz',5.50,'Feijão',4.00,'Bolacha',3.50,'Suco',1.50,'Maçã',3.00,'Prato',30.00)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(tupla)):
    if (pos % 2 == 0):
        print(f'{tupla[pos]:.<30}',end=' ')
    else:
        print(f'R${tupla[pos]:.2f}')
print('-'*40)
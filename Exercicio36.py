# Programa que leia 2 números inteiros e compare-os, da seguinte forma:
# Mostre - O primeiro valor é maior, O segundo valor é maior ou são iguais

val1 = int(input('Digite um valor inteiro qualquer: '))
val2 = int(input('Digite outro valor inteiro qualquer: '))
if val1 > val2:
    print('{} é maior que {}'.format(val1,val2))
elif val2 > val1:
    print('{} é maior que {}'.format(val2,val1))
else:
    print('Não existe maior, {} é igual a {}'.format(val1,val2))
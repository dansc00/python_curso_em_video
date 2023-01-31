# Programa que leia um ano e mostre se ele é bissexto

from time import sleep
ano = int(input('Digite um ano(modelo exemplo - 19XX): '))
print('Analisando...')
sleep(2)
teste1 = ano % 4 #precisa dar 0
teste2 = ano % 100 #precisar ter resto(não ser divisivel)
teste3 = ano % 400 #precisar dar 0, caso não seja divisivel por 4
#Condição 1
if teste1 == 0:
    if teste2 !=  0:
        print('O ano de {} é bissexto'.format(ano))
    else:
        print('O ano de {} não é bissexto'.format(ano))
#Condição 2
if teste1 != 0:
    if teste3 == 0:
        print('O ano de {} é bissexto'.format(ano))
    else:
        print('O ano de {} não é bissexto'.format(ano))




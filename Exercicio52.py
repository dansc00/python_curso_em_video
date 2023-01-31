# Programa que leia o ano de nascimento de sete pessoas e mostre quantas pessoas
# já atingiram a maioridade e quantas ainda são menores

from datetime import date
anoatual = date.today().year
ano = [1,2,3,4,5,6,7]
menor = 0
maior = 0
for x in range(1,8):
    ano[x-1] = int(input('Digite o ano de nacimento da {}ª pessoa: '.format(x)))
for y in range(0,7):
    if anoatual - ano[y] < 18:
        menor += 1
    elif anoatual - ano[y] >= 18:
        maior += 1
print('MAIORES DE IDADE = {} pessoa(s)'.format(maior))
print('MENORES DE IDADE = {} pessoa(s)'.format(menor))







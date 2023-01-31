#Desenvolva um programa que leia quatro valores inteiros pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares

num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor valor: ')))
cont = 0
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 aparece pela primeira vez na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não aparece nenhuma vez.')
print('Os números pares são --> ',end='')
for y in num:
    if y % 2 == 0:
        print(y,end=' ')
        cont += 1
if cont < 1:
    print('Não existem números pares')


# Programa que leia 6 números inteiros e mostre a soma dos pares, desconsidere os ímpares

soma = 0
contt = 0
contp = 0
for x in range(1,7):
   val = int(input('Digite o {}º valor: '.format(x)))
   contt = contt + 1
   if val % 2 == 0:
       soma = soma + val
       contp = contp + 1
print('Foram informados {} valores, destes {} são pares '.format(contt,contp), end='')
print('e a soma entre eles é igual a {}'.format(soma))


















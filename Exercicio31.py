# Programa que leia 3 números e mostre qual é o maior e qual é o menor

num1 = int(input('Digite o valor do primeiro número: '))
num2 = int(input('Digite o valor do segundo número: '))
num3 = int(input('Digite o valor do terceiro número '))
# Pode-se testar para todos os números, mas tem uma maneira mais simples
# Definindo um valor como menor/maior, elimina 1 possibilidade
# Para o menor
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
# Para o maior
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('O maior número é {} e o menor é {}'.format(maior,menor))
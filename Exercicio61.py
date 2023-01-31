# Programa que leia vários números inteiros e pare quando for digitado o número 999
# Mostre quantos números foram digitados e qual foi a soma entre eles (desconsidere o 999)

num = cont = soma = 0
while num!= 999:
    num = int(input('\033[1;35mDigite um número ou 999 para encerrar: '))
    if num != 999:
        soma += num
        cont += 1
print('\033[1;30mForam digitados {} números e a soma entre eles é igual a {}'.format(cont,soma))


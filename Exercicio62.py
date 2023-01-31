# Programa que leia vários números inteiros e no fim mostre a média entre todos e
# qual o maior e menor, pergunte ao usuário se ele quer ou não continuar a indicar valores

opcao = ''
num = cont = soma = media = maior = menor = 0
while opcao!= 'N':
    num = int(input('\033[1;33mDigite um valor inteiro qualquer: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Deseja digitar outro valor?(S/N): ')).strip().upper()
    print('')
media = soma/cont
print('\033[1;31mMÉDIA ENTRE OS VALORES = {:.2f}'.format(media))
print('MAIOR VALOR DIGITADO = {}'.format(maior))
print('MENOR VALOR DIGITADO = {}'.format(menor))


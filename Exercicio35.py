# Programa que leia um número inteiro qualquer e pergunte ao usuário qual será a
# BASE DE CONVERSÃO - 1 para BINÁRIO, 2 para OCTAL, 3 para HEXADECIMAL

num = int(input('\033[1;36mDigite um número inteiro qualquer:\033[m '))
print('\033[;36mEscolha uma base para conversão: ')
print('1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL')
base = int(input('Sua opção: \033[m'))
if base == 1:
    print('\033[;36mVocê escolheu BINÁRIO')
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif base == 2:
    print('Você escolheu OCTAL')
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif base == 3:
    print('Você escolheu HEXADECIMAL')
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('\033[1;31mVOCÊ DIGITOU UM COMANDO INVÁLIDO, TENTE NOVAMENTE')

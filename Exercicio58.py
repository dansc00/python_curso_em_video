# Programa que leia um número inteiro qualquer e mostre seu fatorial

fatorial = 1
print('\033[1;32m# '*10)
print('     \033[1;33mFATORIAL')
print('\033[1;32m# '*10)
val = int(input('\033[1;33mDigite o valor que deseja consultar: '))
c = val
print('{}! = '.format(val),end='')
for x in range(c,0,-1):
    fatorial *= c
    c -= 1
    print('{}'.format(x),end='')
    print(' X ' if c>=1 else ' = ',end='')
print('{}'.format(fatorial))

# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

larg = int(input('Digite a medida de largura do retângulo(Nº inteiro): '))
alt = int(input('Digite a medida de altura do retângulo(Nº inteiro): '))
cont = 0
while cont != alt:
    print('#'*larg,end='')
    cont += 1
    print()

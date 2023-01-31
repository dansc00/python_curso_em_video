larg = int(input('Digite a medida de largura do retângulo(Nº inteiro): '))
alt = int(input('Digite a medida de altura do retângulo(Nº inteiro): '))
cont = 0
while cont != alt:
    if cont == 0:
        print('#'*larg,end='')
    elif cont >= 1 and cont < alt-1:
        print('#'+' '*(larg-2)+'#',end='')
    elif cont == alt - 1:
        print('#'*larg,end='')
    cont += 1
    print()

# Refaça o exercicio 33,porém,adicione o recurso de mostrar qual tipo de triângulo formou:
# EQUILÁTERO - todos lados iguais
# ISÓSCELES - dois lados iguais
# ESCALENO - todos lados diferentes

print('\033[4;32m/\ '*10+'\033[1;30m ANÁLISE DE TRIÂNGULOS '+'\033[4;32m/\ '*10)
a = float(input('\033[;30mDigite o comprimento da reta AB: '))
b = float(input('Digite o comprimento da reta BC: '))
c = float(input('Digite o comprimento da reta AC: '))
if a+b>c and a+c>b and b+c>a:
    print('\033[1;32mAs retas FORMAM UM TRIÂNGULO do tipo:\033[m')
    if a == b and a == c and b == c:
        print('\033[;30mEQUILÁTERO')
    elif a == b or b == c or a == c:
        print('ISÓSCELES')
    elif a != b and b != c and a != c:
        print('ESCALENO')
else:
    print('\033[1;31mAs retas NÃO FORMAM um triângulo')


# Programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo

# A soma do comprimento de 2 retas deve ser maior que o comprimento da terceira
# Pode se usar as 2 menores para somar, já que se a soma dessas for maior que a terceira
# não há como dar resultado diferente

a = float(input('Digite o comprimento da reta AB: '))
b = float(input('Digite o comprimento da reta BC: '))
c = float(input('Digite o comprimento da reta AC: '))

if a+b>c and a+c>b and b+c>a:
    print('A junção das retas AB,BC,AC pode formar um triângulo')
else:
    print('A junção das retas AB,BC,AC não pode formar um triângulo')
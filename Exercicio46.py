# Programa que calcule a soma entre todos números ímpares que são múltiplos de 3
# que se encontram no intervalo de 1 até 500

soma = 0
y = 0
for x in range(1,500,2):
    if x % 3 == 0:
        soma = soma + x #ACUMULADOR
        y = y + 1 #CONTADOR
print('\033[1;36mA soma entre os {} números múltiplos de 3 entre 1 e 500 é igual a {}'.format(y,soma))








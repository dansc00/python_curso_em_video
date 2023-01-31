# Programa que leia o peso e altura de uma pessoa, calcule IMC(Indíce de Massa Corporal)
# Mostre o status de acordo com a tabela:
# Abaixo de - 18.5 = ABAIXO DO PESO
# Entre - 18.5 e 25 = PESO IDEAL
# 25 até 30 = SOBREPESO
# 30 até 40 = OBESIDADE
# Acima de 40 = OBESIDADE MÓRBIDA

print('\033[1;33m-'*10+'\033[1;31m IMC '+'\033[1;33m-'*10)
print('\033[1;31mINDÍCE DE MASSA CORPORAL')
peso = float(input('\033[;33mDigite seu peso(em Kg): '))
alt = float(input('Digite sua altura(em M): '))
imc = peso / (alt ** 2)
print('Resultado - IMC = {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO')
elif imc >= 30 and imc <= 40:
    print('Você está em nivel de OBESIDADE')
elif imc > 40:
    print('Você está em nivel de OBESIDADE MÓRBIDA')


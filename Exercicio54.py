# Programa que leia o nome, idade e sexo de 4 pessoas e mostre:
# A média de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos

nome = ''
idade = 0
sexo = ''
mediaid = 0
testeid = 0
hvelho = ''
nmulheres = 0
for x in range(1,5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(x)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(x)))
    sexo = str(input('Digite o sexo da {}ª pessoa(F/M): '.format(x)))
    print('')
    sexo = sexo.upper().strip()
    mediaid += idade
    if sexo == 'M':
        if idade > testeid:
            testeid = idade
            hvelho = nome
    if sexo == 'F':
        if idade < 20:
            nmulheres += 1
mediaid /= 4
print('A MÉDIA DE IDADE DAS 4 PESSOAS É DE {} ANOS'.format(mediaid))
print('O NOME DO HOMEM MAIS VELHO É {}'.format(hvelho).upper())
print('NO GRUPO, {} MULHERE(S) TEM MENOS DE 20 ANOS'.format(nmulheres))

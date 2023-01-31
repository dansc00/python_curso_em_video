# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date
print('\033[1;31m*-*'*10)
print('\033[1;36m  DEFINIDOR DE CATEGORIA')
print('\033[1;31m*-*'*10)
ano = int(input('\033[;36mDigite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('{} ano(s)/Atleta Categoria: MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('{} ano(s)/Atleta Categoria: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('{} ano(s)/Atleta Categoria: JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('{} ano(s)/Atleta Categoria: SÊNIOR'.format(idade))
elif idade > 20:
    print('{} ano(s)/Atleta Categoria: MASTER'.format(idade))

# Programa que leia o ano de nascimento de um jovem e de acordo com sua idade diga:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# Mostre também o tempo que falta ou que passou do prazo

from datetime import date
print('\033[;32m#'*40)
print('\033[1;30m  BEM VINDO AO SISTEMA DE ALISTAMENTO')
print('\033[;32m#'*40)
ano = int(input('\033[;30mDigite o ano de nascimento do jovem: '))
idade = date.today().year - ano
if idade == 18:
    print('Está na hora de se alistar ao serviço militar!({} anos)'.format(idade))
elif idade < 18:
    print('Ainda não está na hora de se alistar ao serviço militar!')
    print('O jovem possui {} ano(s), então faltam {} ano(s) para o alistamento'.format(idade,18-idade))
elif idade > 18:
    print('O tempo de alistamento foi ultrapassado!')
    print('O jovem possui {} ano(s), então o alistamento deveria ser feito há {} ano(s)'.format(idade,idade-18))

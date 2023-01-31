# Programa que leia o sexo de uma pessoa mas só aceite as opções 'F' ou 'M'
# caso esteja errado peça a digitação novamente até obter o valor correto

sexo = ''
teste = ''
while teste!= 'X':
    sexo = str(input('Digite o seu sexo[M/F]: ').strip().upper())
    if sexo!= 'M' and sexo!= 'F':
        teste = 'f'
        print('')
        print('DIGITE APENAS M PARA MASCULINO OU F PARA FEMININO!')
        print('Por favor, tente novamente')
        print('')
    else:
        teste = 'X'
if sexo == 'M':
    print('')
    print('Sexo Masculino')
elif sexo == 'F':
    print('')
    print('Sexo Feminino')



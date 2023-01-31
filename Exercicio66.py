#Programa que leia a idade e sexo de várias pessoas, a cada pessoa pergunte se o usuário
#deseja continuar a cadastrar. Mostre no final:
#Quantas pessoas tem mais de 18 anos/Quantos são homens/Quantas mulheres tem menos de 20 anos

cont = 0
m18 = nh = n20f = 0
tit = 'CADASTRO'
print('\033[1;30m~'*50)
print(f'\033[1;35m{tit: >25}')
print('\033[1;30m~'*50)
while True:
    cont += 1
    sexo = opcao = ' '
    id = int(input(f'\033[;30mDigite a idade da {cont}ª pessoa: '))
    while sexo not in 'FM':
        sexo = str(input(f'\033[;30mDigite o sexo da {cont}ª pessoa[F/M]: ').strip().upper()[0])
        if sexo not in 'FM':
            print('\033[;31mDIGITE APENAS F PARA FEMININO OU M PARA MASCULINO')
            print('TENTE NOVAMENTE')
            print('\033[1;35m-'*50)
    if id > 18:
        m18 += 1
    if sexo == 'M':
        nh += 1
    if sexo == 'F' and id < 20:
        n20f += 1
    while opcao not in 'SN':
        opcao = str(input('\033[;30mDeseja continuar cadastrando?[S/N]: ').strip().upper()[0])
        if opcao not in 'SN':
            print('\033[;31mDIGITE APENAS S PARA SIM OU N PARA NÃO, TENTE NOVAMENTE')
            print('\033[;35m-'*50)
    print('\033[1;35m-'*50)
    if opcao == 'N':
        break
print(f'\033[1;35mForam cadastradas {cont} pessoas, entre elas: ')
print(f'\033[1;35m{m18} TEM MAIS DE 18 ANOS')
print(f'\033[1;35m{nh} SÃO HOMENS')
print(f'\033[1;35m{n20f} SÃO MULHERES COM MENOS DE 20 ANOS')

# Refaça o exercicio 51, lendo o primeiro termo e a razão de uma PA
# mostre os 10 primeiros termos e pergunte se o usuário quer ver mais alguns termos
# quando ele escolher 0 o programa termina, utilize o WHILE
cont = 0
pa = 0
ntermo = 10
total = 0
termo = int(input('\033[1;31mDigite o valor do 1º termo da PA: '))
razao = int(input('Digite o valor de razão da PA: '))
print('\033[1;32m10 PRIMEIROS TERMOS DA PA:')
print('PA = ({}'.format(termo),end=',')
while ntermo != 0:
    total = total + ntermo
    while cont != total-1:
        pa = termo + razao
        termo = pa
        cont += 1
        print('\033[1;32m{}'.format(termo),end='')
        print(',' if cont<total-1 else ')',end='')
    ntermo = int(input('\n\033[1;31mQuantos termos deseja ver a mais ou 0 para sair: '))
print('\033[1;31mPROGRAMA ENCERRADO!')









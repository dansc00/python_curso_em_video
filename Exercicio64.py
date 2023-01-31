# Programa que mostre a tabuada de vários números, uma de cada vez para cada valor digitado
# O programa deve ser encerrado quando o usuário digitar um valor negativo

print('\033[1;32m='*20)
print('      \033[1;30mTABUADA')
print('\033[1;32m~'*20)
print('')
while True:
    val = int(input('\033[1;30mDigite o valor que deseja consultar a tabuada(VALOR NEGATIVO PARA ENCERRAR): '))
    if val < 0:
        break
    for x in range(1,11):
        print(f'\033[1;32m{val} X {x} = {val*x}')
    print('')
print('\033[1;32mPROGRAMA ENCERRADO')

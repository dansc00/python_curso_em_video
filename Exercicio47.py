# Refaça o exercício 9, mostrando a tabuada de número que o usuário escolher, mas
# utilizando o laço FOR

num = int(input('Digite o número que deseja ver a tabuada: '))
for x in range(1,11):
    print('{} X {} = {}'.format(num,x,num*x))

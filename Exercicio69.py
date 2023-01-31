# Escreva a função maximo que recebe 2 números inteiros como parâmetro e
# devolve o maior deles.
#
# Note que
#
# maximo(3,4) deve devolver 4
#
# maximo(0,-1) deve devolver 0

def maximo(x,y):
    if x>y:
        maxim = x
    else:
        maxim = y
    return maxim
val1 = int(input('Digite um valor inteiro: '))
val2 = int(input('Digite outro valor inteiro: '))
print(f'Maior valor = {maximo(val1,val2)}')

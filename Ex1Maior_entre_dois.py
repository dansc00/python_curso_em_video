def maximo(x,y):
    if x>y:
        maxim = x
    else:
        maxim = y
    return maxim
val1 = int(input('Digite um valor inteiro: '))
val2 = int(input('Digite outro valor inteiro: '))
print(f'Maior valor = {maximo(val1,val2)}')

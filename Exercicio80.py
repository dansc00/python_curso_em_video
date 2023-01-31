# Escreva a função n_primos que recebe um número inteiro(n) maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

def n_primos(x,nfunc):
    cont = tot = 0
    cont2 = 1
    while cont2 != nfunc + 1:
        cont2 += 1
        for z in range(1,nfunc+1):
            if x % z == 0:
                cont += 1
        if cont == 2:
            tot += 1
    return tot

n = result = 0
while True:
    while n < 2:
        n = int(input('Digite um número maior ou igual a 2: '))
        if n < 2:
            print('DIGITE UM VALOR MAIOR OU IGUAL A 2. TENTE NOVAMENTE.')
    print()
    break
for y in range(2,n+1):
    result += n_primos(y,n)
print(f'Existem {result} números primos entre 2 e {n}')









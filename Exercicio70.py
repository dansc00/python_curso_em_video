# Escreva a função maior_primo que recebe um número inteiro maior ou igual
# a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado
# à função
#
# Note que
#
# maior_primo(100) deve devolver 97
#
# maior_primo(7) deve devolver 7
#
# Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até
# o número dado checando se o número é primo ou não; se for, guarde numa variável.
# Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.

def éPrimo(k):
    tot = primo = 0
    for z in range(1,val+1):
        if k % z == 0:
            tot += 1
    if tot == 2:
        primo = k
    return primo

val = 0
while True:
    while val < 2:
        val = int(input('Digite um valor maior ou igual a 2: '))
        if val < 2:
            print('DIGITE UM VALOR MAIOR OU IGUAL A 2, TENTE NOVAMENTE')
    if val >= 2:
        break
for x in range(val, 0, -1):
    maior_primo = éPrimo(x)
    if maior_primo != 0:
        break
print(f"Maior primo = {maior_primo}")



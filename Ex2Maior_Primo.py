def maior_primo(k):
    tot = primo = 0
    for z in range(1,k+1):
        if k % z == 0:
            tot += 1
    if tot == 2:
        primo = k
    return primo

val = int(input('Digite um valor: '))
for x in range(val, 0, -1):
    maiorprimo = maior_primo(x)
    if maiorprimo != 0:
        break
print(maiorprimo)


def remove_repetidos(x):
    x.sort()
    y = -1
    lista2 = []
    while y != len(x):
        y += 1
        if y < len(x):
            if x[y] != x[y-1]:
                lista2.append(x[y])
    return lista2
from random import randint
lista = []
for x in range(0,20):
    lista.append(randint(0,100))
result = remove_repetidos(lista)

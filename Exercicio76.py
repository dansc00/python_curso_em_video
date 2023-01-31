# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
# Dica: Você pode usar lista.sort() ou sorted(lista).

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



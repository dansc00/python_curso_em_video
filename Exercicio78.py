# Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.

def maior_elemento(x):
    return max(x)

from random import randint
lista = []
for x in range(0,20):
    lista.append(randint(0,100))
maior_elemento(lista)

# Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

def soma_elementos(x):
    soma = 0
    for y in range(0,len(x)):
        soma += x[y]
    return soma

from random import randint
lista = []
for x in range(0,20):
    lista.append(randint(0,100))
soma_elementos(lista)


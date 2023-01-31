#Programa que leia e sorteie o nome de 4 alunos em uma certa sequência

import random
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))
lista = [n1,n2,n3,n4]
sorts = random.shuffle(lista) #shuffle - Embaralhar
print('A ordem do sorteio em sequência é: ')
print(lista)
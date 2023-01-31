#Programa que leia o nome de quatro alunos e sorteie uma delas

import random
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))
lista = [n1,n2,n3,n4]
sort = random.choice(lista) #Choice - escolher
print('O escolhido foi {}'.format(sort))
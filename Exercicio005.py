#Faça um programa que leia um número inteiro e mostre na tela seu antecessor e sucessor

val = (int(input('Digite um valor inteiro: ')))
ant = (int(val-1))
suce = (int(val+1))
print('O antecessor de {} é {} e o sucessor é {}'.format(val,ant,suce))

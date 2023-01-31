#Programa que leia o primeiro e último nome de uma pessoa
#e mostre os 2 separadamente

nome = str(input('Digite o nome: ')).strip()
x = nome.find(' ') + 1
y = nome.rfind(' ') + 1
nome1 = nome[:x]
nome2 = nome[y:]
print('O primeiro nome é {}'.format(nome1))
print('O último nome é {}'.format(nome2))

#Poderia usar o split(), criando uma lista de nomes e selecionando o primeiro e último
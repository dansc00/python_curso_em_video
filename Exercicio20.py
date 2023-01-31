#Programa que leia o nome completo de uma pessoa e mostre
#O nome com todas letras maiúsculas
#O nome com todas minúsculas
#Quantas letras no total, sem considerar espaços
#Quantas letras tem o primeiro nome

nome = str(input('Digite um nome completo: ')).strip() #Eliminará os espaços
nmaiusc = nome.upper()
nminusc = nome.lower()
ntotal = len(nome) - nome.count(' ')
ntotal1nome = nome.find(' ') #Procurará o primeiro espaço
print('Nome com letras maiúsculas = {}'.format(nmaiusc))
print('Nome com letras minúsculas = {}'.format(nminusc))
print('Total de letras do nome = {}'.format(ntotal))
print('Total de letras do primeiro nome = {}'.format(ntotal1nome))
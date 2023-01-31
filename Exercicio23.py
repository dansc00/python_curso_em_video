#Programa que leia um nome e diga se ele possui a palavra "Silva"

nome = str(input('Digite um nome: ')).title()
print('O nome possui a palavra "Silva"(True or False): {}'.format('Silva' in nome))
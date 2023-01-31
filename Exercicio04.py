#Faça um programa que leia algo, mostre seu tipo primitivo e todas informações possíveis
#sobre a variável(usando o .is)
x = input('Digite algo: ')
print('O tipo primitivo da informação é ',(type(x)))
#Comando type - tipo

#Mostra se é alfanumérico(possui números e letras)
print(x.isalnum())
#Mostra se é alfabético(possui apenas letras)
print(x.isalpha())
#Possui apenas letras minúsculas
print(x.islower())
#Mostra se possui apenas números
print(x.isnumeric())
#Mostra se só possui espaços
print(x.isspace())
#Está capitalizada(EX: Python)
print(x.istitle())
#Possui apenas letras maiúsculas
print(x.isupper())


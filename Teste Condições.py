# Condição simples
nome = str(input('Qual seu nome? '))
if nome == 'Daniel':
    print('Que nome lindo!')
print('Olá {}'.format(nome))

# Condição composta
nome2 = str(input('Qual seu nome? '))
if nome2 == 'Daniel':
    print('Que nome lindo!')
else:
    print('Seria melhor se chamar Daniel, mas tudo bem.')
print('Olá {}'.format(nome2))

#Simplificado
nome3 = str(input('Qual seu nome? '))
print('Que nome lindo!'if nome3 == 'Daniel' else'Seria melhor se chamar Daniel.')
print('Olá {}'.format(nome3))



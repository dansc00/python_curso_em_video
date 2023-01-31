#Programa que leia uma frase e mostre
#Quantas vezes aparece a letra 'a'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('Analisando frase...')
print('Na frase a letra "A" aparece {} vezes'.format(frase.count('A')))
print('Na frase a letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('Na frase a letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')+1))

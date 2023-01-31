# Programa que leia uma frase e diga se ela é um *PALÍNDROMO
# *lendo-a de trás para frente fica igual. Ex: Após a sopa

frase = str(input('Digite uma frase: ').strip().upper())
nespacos = frase.count(' ')
fraseformat = ''
nfraseformat = ''
if nespacos > 0:
    for x in range(0,nespacos):
        fraseformat = frase.replace(' ','')
else:
    fraseformat = frase
nfraseformat = fraseformat[::-1].upper()
if fraseformat == nfraseformat:
    print('O inverso de "{}" é "{}"'.format(fraseformat,nfraseformat))
    print('Portanto essa frase É UM PALÍNDROMO')
else:
    print('O inverso de "{}" é "{}"'.format(fraseformat,nfraseformat))
    print('Portanto essa frase NÃO É UM PALÍNDROMO')






















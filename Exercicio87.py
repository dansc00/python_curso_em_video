#  Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('Laranja','Goiaba','Banana','Colher','Ovo','Copo','Batata')
for palavra in tupla:
    print(f'\nA palavra {palavra.upper()} possui as vogais', end=' --> ')
    for vog in palavra:
        if vog.lower() in 'aeiou':
            print(vog, end=' ')
# Programa que leia duas notas de um aluno e calcule sua média, mostrando:
# Aprovado se média maior ou igual a 7
# Reprovado se média abaixo de 5
# Recuperação se média entre 5 e 6,9

print('\033[1;31m-'*20+'\033[1;30m MÉDIA '+'\033[1;31m-'*20)
nota1 = float(input('\033[;30mDigite a primeira nota do aluno(Notas entre 0 e 10): '))
nota2 = float(input('Digite a segunda nota do aluno(Notas entre 0 e 10): '))
media = (nota1 + nota2)/2
if nota1>10 or nota1<0 or nota2>10 or nota2<0:
    print('\033[1;31mDIGITE NOTAS APENAS ENTRE 0 E 10, POR FAVOR TENTE NOVAMENTE')
else:
    print('Média = {:.1f}'.format(media))
    if media >= 7:
        print('\033[;32mO aluno foi APROVADO!')
    elif media<5:
        print('\033[;31mO aluno foi REPROVADO!')
    elif media >= 5 and media < 7:
        print('\033[;33mO aluno precisará de RECUPERAÇÃO')



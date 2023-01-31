# Programa que leia um número(entre 0 e 20) e mostre-o por extenso. Uilize TUPLAS.

nms = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
       'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    x = int(input('Digite um número entre 0 e 20: '))
    if x > 20 or x < 0:
        print('DIGITE SOMENTE VALORES ENTRE 0 E 20. TENTE NOVAMENTE.')
        print()
    else:
        break
print(f'O número {x} por extenso é {nms[x]}')




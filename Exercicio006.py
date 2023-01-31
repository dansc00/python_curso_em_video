#Algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada

val = (float(input('Digite um valor: ')))
triplo = (float(val*3))
dobro = (float(val*2))
raiz = (float(val** (1/2)))
print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {}'.format(val,dobro,triplo,raiz))
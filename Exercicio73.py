#Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

#Note que

#maximo(30,14,10) deve devolver 30
#maximo(0,-1, 1) deve devolver 1

def maximo(x,y,z):
    maxi = max(x,y,z)
    return maxi

val1 = int(input('Digite um valor: '))
val2 = int(input('Digite um valor: '))
val3 = int(input('Digite um valor: '))
print(maximo(val1,val2,val3))
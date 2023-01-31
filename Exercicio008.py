#Programa que leia um valor em metros e converta para centimetros e milimetros

val = (float(input('Digite um valor em metros: ')))
cm = (float(val*100))
mm = (float(val*1000))
print('{} metro(s) = {} centímetros e {} milímetros'.format(val,cm,mm))
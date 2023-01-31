#Algoritmo que leia a altura e largura de uma parede em metros, calcule a área
# e a quantidade de tinta necessária para pinta lá.
#Sabendo que cada litro de tinta pinta uma área de 2m².

alt = float(input("Digite a metragem da altura da parede: "))
larg = float(input("Digite a metragem da largura da parede: "))
area = (alt*larg)
tinta = (area/2)
print("Área da parede = {}M²/Quantia de tinta necessária = {}L".format(area,tinta))

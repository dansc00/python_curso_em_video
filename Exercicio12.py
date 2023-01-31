#Algoritmo que leia o preço de um produto e mostre o mesmo com 5% de desconto

val = float(input("Digite o preço do produto: R$"))
val2 = (val*5)/100
print("Preço final = R${:.2f}".format(val2))

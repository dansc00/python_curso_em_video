#Algoritmo que leia o salário de um funcionário e mostre o novo salário com 15% de aumento

sal = float(input("Digite o atual salário do funcionário: R$"))
aumento = (sal*15)/100
sal2 = (sal+aumento)
print("O salário novo do funcionário é = R${:.2f}".format(sal2))
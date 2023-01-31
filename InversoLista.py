def inverso(x):
    for y in range(len(x), 0, -1):
        print(x[y - 1])

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    if lista[-1] == 0:
        del lista[-1]
        break
inverso(lista)

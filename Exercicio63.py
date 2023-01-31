# Programa que leia vários números inteiros e pare quando for digitado o número 999
# Mostre quantos números foram digitados e qual foi a soma entre eles (desconsidere o 999)
# para melhor sintaxe utilize o comando BREAK

cont = soma = 0
while True:
    val = int(input('Digite um valor ou 999 para sair: '))
    if val == 999:
        break
    soma += val
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')

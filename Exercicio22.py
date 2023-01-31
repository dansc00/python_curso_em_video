# Programa que leia o nome de uma cidade e diga se ela começa com a palavra santo

cid = str(input('Digite o nome de uma cidade: ')).title().strip()
cid2 = cid[:5]
print('A cidade começa com a palavra "Santo"(True or False): {}'.format('Santo' in cid2))



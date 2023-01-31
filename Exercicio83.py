# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.


times = ('Flamengo','São Paulo','Corinthians','Fluminense','Internacional','Sport','Cruzeiro','Atlético-MG','Grêmio','Palmeiras','Vasco','América-MG','Atlético-PR','Botafogo','Chapecoense','Vitória','Bahia','Santos','Ceará','Paraná')
print('SEGUNDO DADOS DO DIA 30/05/18 -')
print(f'''Os 5 primeiros times da tabela são: 
1- {times[0]}
2- {times[1]}
3- {times[2]}
4- {times[3]}
5- {times[4]}''')
print()
print(f'''Os últimos 4 colocados são: 
17- {times[-4]}
18- {times[-3]}
19- {times[-2]}
20- {times[-1]}''')
print()
print(f'''Os times em ordem alfabética:
{sorted(times)}''')
print()
pos = 0
for x in times:
    pos += 1
    if x == 'Chapecoense':
        break
print(f'A Chapecoense está na {pos}ª posição - COM FOR')
print()
#OU
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição - COM INDEX')






#Escreva a função vogal que recebe um único caractere como parâmetro
# e devolve True se ele for uma vogal e False se for uma consoante.

#Note que

#vogal("a") deve devolver True

#vogal("b") deve devolver False

#vogal("E") deve devolver True

#Os valores True e False devolvidos devem ser do tipo bool (booleanos)

#Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja,
#precisa estar entre aspas.

def vogal(x):
    if x in 'AEIOU':
        return True
    else:
        return False

while True:
    carac = ''
    while len(carac) > 1 or len(carac) < 1 or carac.isnumeric()== True:
        carac = str(input('Digite uma letra qualquer: ').strip().upper())
        if len(carac) > 1:
            print('DIGITE SOMENTE UMA LETRA, TENTE NOVAMENTE.')
        elif len(carac) < 1:
            print('DIGITE PELO MENOS UMA LETRA, TENTE NOVAMENTE.')
        elif carac.isnumeric() == True:
            print('DIGITE SOMENTE LETRAS, TENTE NOVAMENTE.')
    if len(carac) == 1:
        break
print(f'{carac} é vogal? {vogal(carac)}')

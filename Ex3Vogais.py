def vogal(x):
    if x in 'aeiouAEIOU':
        return True
    else:
        return False

while True:
    carac = ''
    while len(carac) > 1 or len(carac) < 1:
        carac = str(input('Digite uma letra qualquer: ').strip())
        if len(carac) > 1:
            print('DIGITE SOMENTE UMA LETRA, TENTE NOVAMENTE.')
        elif len(carac) < 1:
            print('DIGITE PELO MENOS UMA LETRA, TENTE NOVAMENTE.')
    if len(carac) == 1:
        break
print(f'{carac} é vogal? {vogal(carac)}')

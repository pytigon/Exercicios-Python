cont = 0

for x in range(1, 8):
    p = int(input('Ano que a pessoa {} nasceu: '.format(x)))
    if p <= 2001:
        cont += 1
if cont == 7:
    print('todas as pessoas são maiores de idade nesse grupo')
elif cont >1 and cont<7:
    print('Há {} pessoas maiores de idade nesse grupo'.format(cont))
else:
    print('só há uma pessoa maior de idade nesse grupo')


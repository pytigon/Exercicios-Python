print('  \33[36;4mMaior e menor peso\33[m\n\n')

maior = 0
menor = 0
for x in range(1, 6):
    peso = int(input('Peso da pessoa {}: '.format(x)))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é o de \33[31m{}\33[m e o menor peso é o de \33[33m{}'.format(maior, menor))


print(' NUMEROS PRIMOS')
cont = 0
n = int(input('\33[34mDigite um numero: '))

for x in range(1, 100):
    if n % x == 0:
        cont += 1
if cont == 2:
    print('\33[32mNumero primo detectado')
else:
    print('\33[31mNáo é primo')
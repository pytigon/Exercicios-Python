print(' TABUADA')



while True:
    n = int(input('\nDigite um numero: '))
    if n < 0:
        break
    for x in range(1, 11):
        print(f'{n} x {x} = {n*x}')

print('\nPrograma tabuada encerrado, volte sempre!')

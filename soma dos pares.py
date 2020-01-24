print(' SOMA DOS PARES\n\n')
s=0
for x in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
print('\n\33[32m', 'A soma dos pares é:', s)


num = int(input('Digite um numero: ')), int(input('Digite outro numero: ')),\
     int(input('Digite mais um numero: ')), int(input('Digite um ultimo numero: '))

print(f'Voce digitou os valores {num}')
print(f'Voce Digitou o numero 9, {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 esta na posição {num.index(3)}')
else:
    print('O valor 3 não se encontra em nenhuma posição')

print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='; ')




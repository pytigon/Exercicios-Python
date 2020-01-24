valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Voce digitou {valores}')

print('O maior valor digitado foi o {} nas posições '.format(max(valores)), end='')
for ind, val in enumerate(valores):
    if val == max(valores):
        print(f'{ind}...', end='')

print('\nO menor valor digitado foi o {} nas posições '.format(min(valores)), end='')
for ind, val in enumerate(valores):
    if val == min(valores):
        print(f'{ind}...', end='')

galera = []
dados = []
pesadoes = []
leves = []
maior = menor = c = 0
print('\33[31m-==\33[m'*20)
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    c += 1
    galera.append(dados[:])
    if dados[1] > 99:
        pesadoes.append(dados[:])
        if c == 1:
            maior = dados[1]
        elif dados[1] > maior:
            maior = dados[1]
    else:
        leves.append(dados[:])
        if c == 1:
            menor = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    dados.clear()
    while True:
        escolha = input('Quer continuar?[S/N')
        if escolha in 'NnsS':
            break
    if escolha in 'Nn':
        break
print('\33[31m-==\33[m'*20)
print('Ao todo, você cadastrou {} pessoas'.format(len(galera)))
print(f'O maior peso foi de {maior:.2f}. Peso de ', end='')
for p in pesadoes:
    if p[1] == maior:
        print(p[0], end='; ')

print(f'\nO menor peso foi de {menor:.2f}. Peso de ', end='')
for p in leves:
    if p[1] == menor:
        print(p[0], end='; ')
lista = []
a = 20
n_maior = n_menor = 0
print('-==' * a)
# --------------------------------------------------------------------
while True:
    for x in range(0, 5):
        lista.append(int(input('Digite um valor: ')))
        if x == 0:
            n_menor = n_maior = lista[x]
        else:
            if lista[x] > n_maior:
                n_maior = lista[x]
            if lista[x] < n_menor:
                n_menor = lista[x]
# --------------------------------------------------------------------
    print('-==' * a)
    print(f'Voce digitou os valores {lista}')

    print(f'\nO maior valor é: {n_maior} nas posições ', end='')
    for i, v in enumerate(lista):
        if v == n_maior:
            print(f'{i}...', end='')

    print(f'\nO menor valor é: {n_menor} nas posições ', end='')
    for p, v in enumerate(lista):
        if v == n_menor:
            print(f'{p}... ', end='')
    choice = input('\nDeseja repetir o processo?[s/n]: ')
    if choice in 'Nn':
        break
# --------------------------------------------------------------------

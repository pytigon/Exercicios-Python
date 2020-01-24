material = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 20,
            'Estojo', 9,
            'Caneta', 5,
            'Corretivo', 4)
print('-'*36)
print(f'{"LISTA DE PREÇOS":^36}')
print('-'*36)


for pos in range(0, len(material)):
    if pos %2 == 0:
        print(f'{material[pos]:.<30}', end='')
    else:
        print(f'{material[pos]:>6.2f}')
print('-'*36)
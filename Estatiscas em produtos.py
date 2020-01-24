print('\33[31m-==\33[m' * 15)
print('              \33[34mLOJA SUPER TIGON')
print('\33[31m-==\33[m' * 15)
cont_caro = preco_barato = total = 0
nome_barato = ''
while True:
    produto = input('Nome do produto: ')
    preco = int((input('Preço: R$')))
    if total == 0:
        total = preco
    else:
        total += preco
    if preco > 1000:
        cont_caro += 1
    if preco_barato == 0:
        nome_barato = produto
        preco_barato = preco
    elif preco < preco_barato:
        nome_barato = produto
        preco_barato = preco
    while True:
        choice = input('Quer sair:[s/n]  ')
        if choice in 'NnSs':
            break
    if choice in 'Ss':
        break
print('\33[31m-==\33[m' * 5, end='')
print('\33[34mFIM DO PROGRAMA', end='')
print('\33[31m-==\33[m' * 5)
print(f'O total da compra foi R${total}')
print(f'Temos {cont_caro} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato}, que custou R${preco_barato:.2f}')
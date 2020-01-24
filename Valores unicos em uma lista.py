num = []
cont = 0
while True:
    # Entrada de dados
    n = (int(input('Number> ')))
    if n not in num:
        num.append(n)
    cont += 1
    # Proteção do loop
    if cont == 5:
        while True:
            choice = input('Do you wanna stop?[y/n]')
            if choice in 'nNYy':
                cont = 0
                break
        if choice in 'Yy':
            break
# Finalização
num.sort()
print(f'Os valores digitados foram: {num}')


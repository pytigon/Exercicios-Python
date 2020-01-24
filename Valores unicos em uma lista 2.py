num = []

while True:
    # Entrada de dados
    n = (int(input('Number> ')))
    if n not in num:
        num.append(n)
        print('Adicionado com sucesso!')
    else:
        print('Numero já adicionado!')
    # Loop
    while True:
        escolha = input('Quer continuar?[S/N]\n>>>')
        if escolha in 'NnsS':
            break
    if escolha in 'Nn':
        break
# Finalização
num.sort()
print(f'Os valores digitados foram: {num}')
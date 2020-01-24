print('\33[31m-==\33[m' * 20)

# DECLARAÇÃO DE VARIAVEIS
galera = []
info = []
peso_min = peso_max = 0

# ADQUIRINDO DADOS
while True:
    info.append(input('Nome: '))
    info.append(float(input('Peso: ')))

# ANALISANDO DADOS PT1
    if len(galera) == 0:
        peso_max = peso_min = info[1]
    else:
        if info[1] > peso_max:
            peso_max = info[1]
        if info[1] < peso_min:
            peso_min = info[1]

    galera.append(info[:])
    info.clear()

# SAÍDA DO LOOP
    while True:
        escolha = input('Quer continuar?[S/N]')
        if escolha in 'NnsS':
            break
    if escolha in 'Nn':
        break

# VISUALIZAÇÃO DO RESULTADO
print('\33[31m-==\33[m' * 20)
print(f'Ao todo, vc cadastrou {len(galera)} pessoas.')

# ANALISANDO DADOS PT2
print(f'O maior peso foi de {peso_max}kg. Peso de ', end='')
for pessoa in galera:
    if pessoa[1] == peso_max:
        print(pessoa[0], end=', ')
print(f'\nO menor peso foi de {peso_min}kg. Peso de ', end='')
for pessoa in galera:
    if pessoa[1] == peso_min:
        print(pessoa[0], end=', ')

# CONCLUSÃO
print('\nObrigado volte sempre!')
print('\33[31m-==\33[m' * 20)

print('\33[36m=====CADASTRO DE USUARIOS=====\33[m\n')
mais18 = boy = girl = m = 0

while True:
    print('-' * 30)
    print('   CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        mais18 += 1
    sexo = input('Sexo: ')
    while sexo not in 'FfMm':
        sexo = input('Sexo: ')
        if sexo in 'Mm':
            boy += 1
        elif idade < 20:
            girl += 1
    while True:
        print('-' * 30)
        choice = input('Quer continuar? ')
        if choice in 'Ss':
            break
        elif choice in 'Nn':
            break
    if choice in 'Nn':
        break
print('\nTotal de pessoas com mais de 18 anos: {}'.format(mais18))
print(f'Ao todo temos {boy} homens cadastrados')
print(f'E temos {girl} Mulher com menos de 20 anos')



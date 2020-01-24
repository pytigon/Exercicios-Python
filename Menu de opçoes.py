import time
print('  \n\33[36;4mMENU DE OPÇÕES\33[m\n\n')

a = int(input('Variável \33[31mA\33[m: '))
b = int(input('Variável \33[34mB\33[m: '))
print('\33[31m-==\33[m' * 10)

opcao = 0
while opcao != 6:
    termo = a
    cont = 1
    cont2 = 10
    cont_termo = 0
    print('\nOPÇÕES:\n')
    opcao = int(input('''[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Progressão aritmética
[6]Sair
\33[31m>>>>\33[m '''))
    if opcao == 1:
        print('\n  \33[31mSOMAR\33[m')
        print('{} + {} = \33[32m{}\33[m\n'.format(a, b, a+b))
    elif opcao == 2:
        print('\n  \33[32mMULTIPLICAR\33[m')
        print('{} * {} = {}'.format(a, b, a*b))
    elif opcao == 3:
        print('\n  \33[36mQUAL É MAIOR\33[m')
        if a > b:
            print('{} é \33[32mMAIOR\33[m que {}'.format(a, b))
        else:
            print('{} é \33[32mMAIOR\33[m que {}'.format(b, a))
    elif opcao == 4:
        a = int(input('\nVariável \33[31mA\33[m: '))
        b = int(input('Variável \33[34mB\33[m: '))
    elif opcao == 5:
        print('  \33[34;4mProgressão aritmética\33[m')
        while cont2 != 0:
            print('-==' * 25)
            while cont <= cont2:
                print('{} -> '.format(termo), end='')
                termo += b
                cont += 1
                cont_termo += 1
            print('\33[31mPausa\33[m')
            print('-==' * 25)
            cont = 1
            cont2 = int(input('Quantos termos você quer mostrar a mais?\n\33[31m>>>>\33[m '))
            if cont2 == 0:
                print('Progressão finalizada com \33[31m{}\33[m termos mostrados'.format(cont_termo))
    elif opcao == 6:
        print('\n Finaliando o sistema', end='')
        for t in range(4):
            time.sleep(0.5)
            print('.', end='')
    else:
        print('\n \33[31mDigite um número válido.\33[m')

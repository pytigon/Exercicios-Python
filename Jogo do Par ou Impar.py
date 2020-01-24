from random import randint as r
from time import sleep as t

print('   \n\33[31mJogo do par ou impar\33[m')

cont = 0
while True:
    vc = int(input('\nDiga um valor: '))
    pc = r(1, 10)
    result = vc + pc
    choice = str(input('Par ou Impar[p/i]: '))

    t(0.5)
    print('\nPar')
    t(0.5)
    print('ou')
    t(0.5)
    print('Impar\n')
    t(0.5)

    if choice == 'p':
        if result %2 == 0:
            print(f'Voce jogou {vc}\nComputador jogou {pc}\nTOTAL: {result}\n\nVoce ganhou')
            cont += 1
        else:
            print(f'Voce jogou {vc}\nComputador jogou {pc}\nTOTAL: {result}\n\nVoce perdeu')
            break
    elif choice == 'i':
        if result %2 == 1:
            print(f'Voce jogou {vc}\nComputador jogou {pc}\nTOTAL: {result}\n\nVoce ganhou')
            cont += 1
        else:
            print(f'Voce jogou {vc}\nComputador jogou {pc}\nTOTAL: {result}\n\nVoce perdeu')
            break
    elif choice != 'p' or vc != int:
        print('Por favor digite somente P(par) ou I(impar)')
print('Vc ganhou {} vezes'.format(cont))


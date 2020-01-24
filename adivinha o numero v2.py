from random import randint

print('  \n\33[36;4mADVINHE O NUMERO 2\33[m\n\n')

num = randint(1, 10)

x = 0
while x != num:
    x = int(input('Qual o número?\n>>> '))
    if x != num:
        print('Voce errou, tente novamente.')
print('Voce acertou, legal')


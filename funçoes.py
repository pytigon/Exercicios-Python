from time import sleep


def contagem(i, f, p):
    tempo = 0.3
    if p == 0:
        p = 1
    if p < 0:
        p = p * -1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        while i <= f:
            print(i, end=' ')
            sleep(tempo)
            i += p
        print('Fim!')
    elif i > f:
        while i >= f:
            print(i, end=' ')
            sleep(tempo)
            i -= p
        print('Fim!')
    else:
        print('Não é permitido digitar 0!')


i = 1
f = 10
p = 1
contagem(i, f, p)
i = 10
f = 1
p = 2
contagem(i, f, p)
while True:
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('inicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    contagem(i, f, p)

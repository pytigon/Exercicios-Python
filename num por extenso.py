tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco',\
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', \
        'doze', 'treze', 'catoreze', 'quize', 'dezesseis',\
        'dezzessete', 'dezoito', 'dezenove', 'vinte'
while True:
    ask = int(input('Digite um numero entre 0 e 20: '))
    while ask not in range(0, 20):
         ask = int(input('Tente novamente: '))
    if 0<= ask <= 20:
        print(f'Voce digitou o numero {tupla[ask]}')
        choice = input('Quer sair[s/n]: ')
        if choice in 's':
            break


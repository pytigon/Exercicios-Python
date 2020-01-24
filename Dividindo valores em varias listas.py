lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    while True:
        choice = input('Quer continuar:[S/N] ')
        if choice in 'NnSs':
            break
    if choice in 'Nn':
        break
print('-=='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}\nA lista de impares é {impar}')
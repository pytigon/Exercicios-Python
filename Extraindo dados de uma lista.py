lista = []
while True:
    lista.append(input('Digite um valor: '))
    while True:
        choice = input('Quer continuar:[S/N] ')
        if choice in 'NnSs':
            break
    if choice in 'Nn':
        break
print('-=='*20)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em decrescente são:{lista}')
if 5 in lista:
    print('O valor 5 fa parte da lista')
else:
    print('O valor 5 nao faz parte da lista')

num = [0, 3, 4, 3, 5, 6, 3, 1, ]
num[3] = 9
num.append(2)
num.insert(0, 8)
num.remove(3)
num.pop()
print(f'A lista criada é: {num}')
print('Essa lista tem {} elementos\n\n'.format(len(num)))

# -----------------------------------------------------------

lista = []
lista.append(3)
lista.append(4)
lista.append(1)
lista.append(9)
for p, n in enumerate(lista):
    print(f'Na posição {p} encontrei o numero {n}')



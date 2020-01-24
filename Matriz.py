matriz = [[], []]
linha = coluna = 0
for c in range(0, 9):
    n = int(input(F'Digite um valor para [{linha, coluna}]: '))
    coluna += 1
    if coluna == 3:
        linha += 1
        
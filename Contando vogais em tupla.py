palavras = ('carro', 'moto', 'bicicleta', 'aviao', 'batata', 'morena', 'cebra')

vogais = 'aeiou'
cont_vogais = 0

for p in palavras:
    print(f'\nA palavra {p} possui ', end='')
    for letra in p:

        if letra in vogais:
           print(f' {letra}, ',end='')
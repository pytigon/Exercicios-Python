from playsound import playsound

quest = 'Informe um número: '

num = str(input(quest)) .strip()
print('Analisando o número', num)

separa = ' '.join(num)

lista = separa.split()

print('Unidade: ', lista[0])
print('Dezena: ', lista[1])
print('Centena: ', lista[2])
print('Milhar: ', lista[3])

playsound('guitar.mp3')

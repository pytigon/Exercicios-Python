from playsound import playsound

quest ='Qual o seu nome? '

nome = str(input(quest)).strip()


split = nome.split()

print('1 - {}\n2 - {}\nNumero de letras - {}'.format(nome.upper(), nome.lower(), (len(nome) - nome.count(' '))))


print('Seu primeiro nome tem {} letras'.format(len(split[0])))
playsound('guitar.mp3')

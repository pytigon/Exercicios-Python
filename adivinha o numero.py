import random, playsound
texto = 'Hey, eu pensei em um número entre 1 e 5\nAdivinhe qual é: '

n = random.randint(1, 5)
ans = int(input(texto))


if ans == n:
    print('\nParabens! Você acertou')
    playsound.playsound('homer.mp3')
else:
    print('\nErrrou, eu pensei no número ', n)
    playsound.playsound('errou.mp3')

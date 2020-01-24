import math
import playsound

ang = float(input('Digite o angulo que você deseja: '))

rad = math.radians(ang)


print('\nO angulo de {} tem o seno de {:.2f}'.format(ang, math.sin(rad)))
print('\nO angulo de {} tem o coseno de {:.2f}'.format(ang, math.cos(rad)))
print('\nO angulo de {} tem a tangente de {:.2f}'.format(ang, math.tan(rad)))


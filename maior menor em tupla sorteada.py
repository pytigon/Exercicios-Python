from random import randint as r

t = r(0, 9), r(0, 9), r(0, 9), r(0, 9), r(0, 9)

print(f'Os valores sorteados foram: {t[0]} {t[1]} {t[2]} {t[3]} {t[4]}')
print(f'o maior valor sorteado foi {max(t)}')
print(f'o menor valor sorteado foi {min(t)}')
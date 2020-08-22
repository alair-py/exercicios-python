import math

catA = float(input('Valor do cateto adjacente: '))
catO = float(input('Valor do cateto oposto: '))

hipot = math.hypot(catA, catO)

print(f'O valor da hipotenusa é {hipot:2f}')

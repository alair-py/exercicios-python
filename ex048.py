# SOMA IMPARES MULTIPLOS DE 3

s = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print(f'A soma dos impares multiplos de 3, de 1 até 500 é {s}')
